🛡️ CipherFile v2.0 - Asenkron AES Güvenliği

"CipherFile", dosyalarınızı askeri düzeyde 'AES-256' algoritmasıyla şifreleyen ve işlem sonrası orijinal dosyayı adli bilişim teknikleriyle geri döndürülemeyecek şekilde imha eden (secure wipe) masaüstü bir güvenlik aracıdır.

✨ Öne Çıkan Özellikler

Asenkron İşlem (Threading): Şifreleme ve çözme işlemleri arka planda yürütülür; bu sayede büyük dosyalarda bile uygulama arayüzü donmaz.

Güvenli Silme (Data Wiping): Orijinal dosya silinmeden önce üzerine `secrets` kütüphanesi ile rastgele baytlar yazılarak fiziksel disk üzerinden kurtarılması engellenir.

Modern Arayüz: `CustomTkinter` kütüphanesi ile karanlık mod destekli, kullanıcı dostu ve şık bir GUI.

Kriptografik Güç: Dosya şifreleme standardı olarak güvenilir `pyAesCrypt` (AES-256-CBC) kullanır.

🚀 Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. Depoyu Klonlayın:
```bash
git clone https://github.com/kullaniciadi/CipherFile.git
cd CipherFile

```


2. Gerekli Kütüphaneleri Yükleyin:
```bash
pip install pyAesCrypt customtkinter

```


3. Uygulamayı Başlatın:
```bash
python kriptolama1.1.py

```


 🛠️ Teknik Detaylar

Güvenli İmha Mekanizması

Uygulama, `guvenli_sil` fonksiyonu ile dosya boyutunu analiz eder ve `secrets.token_bytes` kullanarak dosyanın olduğu sektöre rastgele veriler yazar. Bu işlem, dosya silinse bile veri kurtarma yazılımlarının anlamlı bir veriye ulaşmasını imkansız hale getirir.

  Şifreleme Akışı

1. Seçim: Kullanıcı dosya yolunu ve anahtar şifresini belirler.
2. Arka Plan İşçisi: `threading.Thread` başlatılarak GUI'den bağımsız bir işlem süreci oluşturulur.
3. Şifreleme: Dosya `.aes` uzantısıyla şifrelenmiş bir kopyaya dönüştürülür.
4. İmha: İşlem başarılıysa kaynak dosya "Secure Wipe" yöntemiyle silinir.


⚠️ Uyarı

Şifrenizi Unutmayın! AES-256 şifreleme algoritmasında "şifremi unuttum" seçeneği yoktur. Şifrenizi kaybetmeniz durumunda verilerinize erişim sağlamak matematiksel olarak (brute-force dışında) mümkün değildir.


👥 Grup Üyeleri

* [Asya ALTAN]
* [Yağız Yasin CAN]
* [Rabia Nur KUZÇALI]
* [Ege Talha KURBAN]
