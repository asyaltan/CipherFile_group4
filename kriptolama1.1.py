import pyAesCrypt
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
import secrets

# GÜVENLİ SİLME (DATA WIPING) FONKSİYONU
def guvenli_sil(dosya_yolu):
    try:
        if os.path.exists(dosya_yolu):
            boyut = os.path.getsize(dosya_yolu)
            with open(dosya_yolu, "ba+", buffering=0) as f:
                f.write(secrets.token_bytes(boyut))
            os.remove(dosya_yolu)
    except:
        if os.path.exists(dosya_yolu):
            os.remove(dosya_yolu)

# ŞİFRELEME FONKSİYONLARI

def sifrele(dosya, sifre):
    bufferSize = 512 * 1024
    sifreli_dosya = str(dosya) + ".aes"
    try:
        pyAesCrypt.encryptFile(str(dosya), sifreli_dosya, sifre, bufferSize)
        guvenli_sil(dosya)
        return True # İşlem başarıyla bitti sinyali
    except Exception as e:
        messagebox.showerror("Hata", f"Şifreleme sırasında bir hata oluştu: {e}")
        return False # Bir şeyler ters gitti sinyali

def sifrecoz(dosya, sifre):
    bufferSize = 512 * 1024
    if str(dosya).endswith(".aes"):
        cozulmus_dosya = str(dosya)[:-4]
    else:
        cozulmus_dosya = "cozulmus_" + str(dosya)

    try:
        pyAesCrypt.decryptFile(str(dosya), cozulmus_dosya, sifre, bufferSize)
        guvenli_sil(dosya)
        return True # İşlem başarıyla bitti sinyali
    except ValueError:
        messagebox.showerror("Hata", "Şifre yanlış! Lütfen tekrar deneyin.")
        return False
    except Exception as e:
        messagebox.showerror("Hata", f"Şifre çözme hatası: {e}")
        return False

# GUI ARA FONKSİYONLARI

def encrypt_ui():
    dosya = selected_file.get()
    sifre = password_entry.get()
    if dosya == "" or sifre == "":
        messagebox.showerror("Hata", "Dosya veya şifre boş olamaz.")
        return
    
    # EĞER (if) fonksiyon True dönerse başarı mesajını göster
    if sifrele(dosya, sifre):
        messagebox.showinfo("Başarılı", "Dosya şifrelendi, orijinali silindi.")

def decrypt_ui():
    dosya = selected_file.get()
    sifre = password_entry.get()
    if dosya == "" or sifre == "":
        messagebox.showerror("Hata", "Dosya veya şifre boş olamaz.")
        return
    
    # EĞER (if) fonksiyon True dönerse başarı mesajını göster
    if sifrecoz(dosya, sifre):
        messagebox.showinfo("Başarılı", "Şifre çözüldü, .aes dosyası silindi.")

# GUI PENCERE OLUŞTURMA
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x400")
app.title("CipherFile - AES Şifreleme")

selected_file = ctk.StringVar()
file_entry = ctk.CTkEntry(app, textvariable=selected_file, width=300)
file_entry.pack(pady=20)

file_button = ctk.CTkButton(app, text="Dosya Seç", command=lambda: selected_file.set(filedialog.askopenfilename()))
file_button.pack(pady=5)

password_entry = ctk.CTkEntry(app, placeholder_text="Şifre girin", show="*")
password_entry.pack(pady=10)

encrypt_button = ctk.CTkButton(app, text="Şifrele", command=encrypt_ui)
encrypt_button.pack(pady=5)

decrypt_button = ctk.CTkButton(app, text="Şifre Çöz", command=decrypt_ui)
decrypt_button.pack(pady=5)

app.mainloop()