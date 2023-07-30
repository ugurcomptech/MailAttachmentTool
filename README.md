# Mail Attachment Tool

Bu Python betiği, belirli dosya uzantılarına sahip dosyaları tarar ve bu dosyaları e-posta ile belirtilen alıcıya gönderir. Aynı zamanda dosyaları .exe dosyasına dönüştürme yeteneğine sahiptir.

## Kurulum

1. Öncelikle, projeyi bilgisayarınıza indirin veya klonlayın:


   ```python
   git clone https://github.com/KULLANICI_ADI/MailAttachmentTool.git
   cd MailAttachmentTool
    ```


2. Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırın:

   ```python
      pip install -r requirements.txt
    ```


## Kullanım

1. Proje klasöründe, `MailAttach.py` dosyasını çalıştırın:

   ```python
      python MailAttach.py
    ```


2. Program çalıştığında, sırasıyla aşağıdaki bilgileri girin:

- -s, --sender-email:(Sender Email): E-posta gönderenin e-posta adresi.
- -p, --passowrd:(Sender Password): E-posta gönderenin e-posta şifresi.
- -r. --receiver-email: Dosyaların gönderileceği alıcı e-posta adresi.
- -d, --folder-path: Dosyaların taramasını istediğiniz klasörün yolunu girin (örn: C:\my_folder).
- -n, --file-name: Taramak istediğiniz dosya uzantılarını boşluklarla ayrılarak girin (örn: pdf jpg png).
- -e, --file-extensions: .exe dosyasına dönüştürülecek betiğin adını girin (örn: MyAttachmentTool).

3. Gerekli bilgileri girdikten sonra, program belirttiğiniz dosya uzantılarına sahip dosyaları taramaya başlayacak ve e-posta ile belirtilen alıcıya gönderecektir.

## Dikkat!

- Gönderen e-posta adresi ve şifresi, güvenlik nedenleriyle kodunuzda doğrudan yer almalıdır. Bu bilgileri kodunuzu paylaşırken veya GitHub gibi platformlarda paylaşırken dikkatli olunuz.

- Projeyi çalıştırmadan önce, bilgisayarınızda projenin taramak istediğiniz klasörde uygun dosyalar olduğundan emin olunuz. E-posta gönderimi yapmadan önce alıcı e-posta adresini doğrulayınız.

- Proje, Python 3 ve üzeri sürümlerinde çalışacaktır. Gerekli paketleri `requirements.txt` dosyasını kullanarak yükleyebilirsiniz.

- Proje dosyalarınızı `.gitignore` dosyasına eklemeyi unutmayın. Bu sayede gereksiz dosyaların sürüm kontrolüne eklenmesi önlenir.



## Lisans

[![License: GPL](https://img.shields.io/badge/License-GPL-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)



Bu projeyi [GNU Genel Kamu Lisansı (GPL)](https://www.gnu.org/licenses/gpl-3.0) altında lisansladık. Lisansın tam açıklamasını [GNU web sitesinde](https://www.gnu.org/licenses/gpl-3.0) bulabilirsiniz.

