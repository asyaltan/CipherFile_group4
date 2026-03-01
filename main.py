import pyAesCrypt
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
import secrets
import threading 

# ŞİFRE GİZLEME/GÖSTERME FONKSİYONU
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        show_button.configure(text="👁️‍🗨️")
    else:
        password_entry.configure(show="*")
        show_button.configure(text="👁️")
        
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
        app.after(0, lambda: islem_tamamlandi(False, islem_turu, str(e)))

# ARAYÜZ YÖNETİMİ
def baslat(islem_turu):
    dosya = selected_file.get()
    sifre = password_entry.get()
    
    if not dosya or not sifre:
        messagebox.showwarning("Eksik Bilgi", "Lütfen dosya seçin ve bir şifre belirleyin.")
        return

    progress_bar.pack(pady=10)
    progress_bar.start()
    encrypt_button.configure(state="disabled")
    decrypt_button.configure(state="disabled")

    threading.Thread(target=islem_yap_arka_plan, args=(islem_turu, dosya, sifre), daemon=True).start()

def islem_tamamlandi(basari, tur, hata=""):
    progress_bar.stop()
    progress_bar.pack_forget()
    encrypt_button.configure(state="normal")
    decrypt_button.configure(state="normal")

    if basari:
        islem_adi = "şifrelendi" if tur == "sifrele" else "çözüldü"
        messagebox.showinfo("Başarılı", f"Dosya güvenle {islem_adi} ve orijinali imha edildi.")
    else:
        messagebox.showerror("İşlem Başarısız", f"Hata detayı: {hata}")

# ANA PENCERE TASARIMI 
ctk.set_appearance_mode("Dark")
app = ctk.CTk()
app.geometry("500x480")
app.title("CipherFile v2.0 - Asenkron AES Güvenliği")

selected_file = ctk.StringVar()
ctk.CTkEntry(app, textvariable=selected_file, width=350, placeholder_text="Dosya yolu...").pack(pady=20)
ctk.CTkButton(app, text="📂 Dosya Seç", command=lambda: selected_file.set(filedialog.askopenfilename())).pack(pady=5)

# ŞİFRE GİRİŞ ALANI (FRAME İÇİNDE)
password_frame = ctk.CTkFrame(app, fg_color="transparent")
password_frame.pack(pady=10)

password_entry = ctk.CTkEntry(password_frame, placeholder_text="Anahtar Şifre", show="*", width=280)
password_entry.pack(side="left", padx=5)

show_button = ctk.CTkButton(password_frame, text="👁️", width=40, command=toggle_password)
show_button.pack(side="left")

# BUTONLAR VE İLERLEME ÇUBUĞU
encrypt_button = ctk.CTkButton(app, text="🔒 Şifrele", fg_color="#D22B2B", command=lambda: baslat("sifrele"))
encrypt_button.pack(pady=5)

decrypt_button = ctk.CTkButton(app, text="🔓 Şifre Çöz", fg_color="#228B22", command=lambda: baslat("coz"))
decrypt_button.pack(pady=5)

progress_bar = ctk.CTkProgressBar(app, width=350, mode="indeterminate", progress_color="#FFCC00")

app.mainloop()