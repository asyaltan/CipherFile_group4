import pyAesCrypt
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
import secrets
import threading # Asenkron (arka plan) işlemler için gerekli kütüphane

# GÜVENLİ SİLME (DATA WIPING) FONKSİYONU
def guvenli_sil(dosya_yolu):
    """Dosyanın üzerine rastgele baytlar yazarak adli bilişimle geri döndürülmesini engeller."""
    try:
        if os.path.exists(dosya_yolu):
            boyut = os.path.getsize(dosya_yolu)
            with open(dosya_yolu, "ba+", buffering=0) as f:
                f.write(secrets.token_bytes(boyut))
            os.remove(dosya_yolu)
    except:
        if os.path.exists(dosya_yolu):
            os.remove(dosya_yolu)

# ARKA PLAN İŞÇİSİ (WORKER THREAD)
def islem_yap_arka_plan(islem_turu, dosya, sifre):
    """Ağır şifreleme işlemini arayüzü dondurmadan arka planda yürüten fonksiyon."""
    bufferSize = 512 * 1024
    success = False
    
    try:
        if islem_turu == "sifrele":
            sifreli_dosya = str(dosya) + ".aes"
            pyAesCrypt.encryptFile(str(dosya), sifreli_dosya, sifre, bufferSize)
            guvenli_sil(dosya)
            success = True
        else:
            if str(dosya).endswith(".aes"):
                cozulmus_dosya = str(dosya)[:-4]
            else:
                cozulmus_dosya = "cozulmus_" + str(dosya)
            pyAesCrypt.decryptFile(str(dosya), cozulmus_dosya, sifre, bufferSize)
            guvenli_sil(dosya)
            success = True
            
        app.after(0, lambda: islem_tamamlandi(success, islem_turu))
        
    except Exception as e:
        # Hata durumunda hata mesajını arayüze gönder
        app.after(0, lambda: islem_tamamlandi(False, islem_turu, str(e)))

# ARAYÜZ YÖNETİMİ

def baslat(islem_turu):
    """Butona basıldığında hazırlıkları yapar ve arka plan işçisini başlatır."""
    dosya = selected_file.get()
    sifre = password_entry.get()
    
    if not dosya or not sifre:
        messagebox.showwarning("Eksik Bilgi", "Lütfen dosya seçin ve bir şifre belirleyin.")
        return

    # İşlem başlarken arayüz elemanlarını hazırla ve kilitle
    progress_bar.set(0)
    progress_bar.pack(pady=10) # İlerleme çubuğunu görünür yap
    progress_bar.start() # Animasyonu başlat
    encrypt_button.configure(state="disabled")
    decrypt_button.configure(state="disabled")

    # Çoklu iş parçacığı (Threading) başlatılıyor
    threading.Thread(target=islem_yap_arka_plan, args=(islem_turu, dosya, sifre), daemon=True).start()

def islem_tamamlandi(basari, tur, hata=""):
    """Arka plandaki işlem bittiğinde arayüzü eski haline getiren geri çağırma fonksiyonu."""
    progress_bar.stop()
    progress_bar.pack_forget() # Çubuğu gizle
    encrypt_button.configure(state="normal")
    decrypt_button.configure(state="normal")

    if basari:
        islem_adi = "şifrelendi" if tur == "sifrele" else "çözüldü"
        messagebox.showinfo("Başarılı", f"Dosya güvenle {islem_adi} ve orijinali imha edildi.")
    else:
        # Şifre yanlışsa pyAesCrypt ValueError fırlatır
        messagebox.showerror("İşlem Başarısız", f"Hata detayı: {hata}")

# ANA PENCERE TASARIMI 
ctk.set_appearance_mode("Dark")
app = ctk.CTk()
app.geometry("500x480")
app.title("CipherFile v2.0 - Asenkron AES Güvenliği")

selected_file = ctk.StringVar()
# Dosya yolu giriş alanı
ctk.CTkEntry(app, textvariable=selected_file, width=350, placeholder_text="Dosya yolu...").pack(pady=20)
# Dosya seçme diyaloğu butonu
ctk.CTkButton(app, text="📂 Dosya Seç", command=lambda: selected_file.set(filedialog.askopenfilename())).pack(pady=5)

# Şifre giriş alanı 
password_entry = ctk.CTkEntry(app, placeholder_text="Anahtar Şifre", show="*", width=350)
password_entry.pack(pady=10)

# Şifreleme ve Çözme butonları
encrypt_button = ctk.CTkButton(app, text="🔒 Şifrele", fg_color="#D22B2B", command=lambda: baslat("sifrele"))
encrypt_button.pack(pady=5)

decrypt_button = ctk.CTkButton(app, text="🔓 Şifre Çöz", fg_color="#228B22", command=lambda: baslat("coz"))
decrypt_button.pack(pady=5)

# Dinamik ilerleme çubuğu (İşlem sırasında görünür)
progress_bar = ctk.CTkProgressBar(app, width=350, mode="indeterminate", progress_color="#FFCC00")


app.mainloop()
