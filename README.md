🛡️ CipherFile v2.0 - Asenkron AES Güvenliği

"CipherFile", dosyalarınızı askeri düzeyde 'AES-256' algoritmasıyla şifreleyen ve işlem sonrası orijinal dosyayı adli bilişim teknikleriyle geri döndürülemeyecek şekilde imha eden (Secure Wipe) masaüstü bir güvenlik aracıdır.

✨ Öne Çıkan Özellikler

Asenkron İşlem (Threading): Şifreleme ve çözme işlemleri arka planda yürütülür; bu sayede büyük dosyalarda bile "Main Thread" kilitlenmez ve uygulama arayüzü her zaman akıcı kalır.

Güvenli Silme (Data Wiping): Orijinal dosya silinmeden önce üzerine `secrets` kütüphanesi ile rastgele baytlar yazılır. Bu, verinin fiziksel disk üzerinden kurtarılmasını (recovery) imkansız hale getirir.

Modern Arayüz (GUI): `CustomTkinter` kütüphanesi kullanılarak geliştirilen, karanlık mod (Dark Mode) destekli, kullanıcı dostu ve şık bir GUI.

Kriptografik Güç: Dosya şifreleme standardı olarak güvenilir `pyAesCrypt` (AES-256-CBC)ile tam güvenilirlik sağlar.

🚀 Kurulum ve Çalıştırma

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
python main.py

```


 🛠️ Teknik Detaylar

Güvenli İmha Mekanizması

Uygulama, `guvenli_sil` fonksiyonu ile dosya boyutunu analiz eder ve `secrets.token_bytes` kullanarak dosyanın olduğu sektöre rastgele veriler yazar. Bu işlem, dosya silinse bile veri kurtarma yazılımlarının anlamlı bir veriye ulaşmasını imkansız hale getirir.

  Şifreleme Akışı (Workflow)

1. Girdi (Input): Kullanıcı dosya yolunu ve AES-256 anahtar şifresini belirler.
2. Asenkron Yapı: `threading.Thread` başlatılarak GUI'den bağımsız bir işlem süreci oluşturulur.
3. Kriptografik Süreç: Dosya `.aes` uzantısıyla şifrelenmiş bir kopyaya dönüştürülür.
4. Güvenli İmha (Secure Wipe): Şifre doğrulama adımı başarıyla tamamlandığında, kaynak dosya "Secure Wipe" yöntemi ile kalıcı olarak imha edilir.


⚠️ Uyarı

Şifrenizi Unutmayın! AES-256 şifreleme algoritmasında "şifremi unuttum" seçeneği yoktur. Şifrenizi kaybetmeniz durumunda verilerinize erişim sağlamak matematiksel olarak (brute-force dışında) mümkün değildir.


👥 Grup Üyeleri

* [Asya ALTAN]
* [Yağız Yasin CAN]
* [Rabia Nur KUZÇALI]
* [Ege Talha KURBAN]

