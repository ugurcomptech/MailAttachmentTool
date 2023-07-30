# Mail Attachment Tool


MailAttach, belirtilen dosya uzantılarına sahip dosyaları belirtilen e-posta adresine göndermek için kullanılan Python betiğidir.


## Kurulum

1. Öncelikle, projeyi bilgisayarınıza indirin veya klonlayın:


   ```python
   https://github.com/ugurcomptech/MailAttachmentTool.git
   cd MailAttachmentTool
    ```


2. Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırın:

   ```python
      pip install -r requirements.txt
    ```


## Kullanım

1. Proje klasöründe, `MailAttach.py` dosyasını çalıştırın:

   ```python
   py MailAttach.py -s example@gmail.com -p example_passowrd  -r  example@gmail.com@gmail.com -d C:/Users -f png
    ```


2. Program çalıştığında, sırasıyla aşağıdaki bilgileri girin:

- -s, --sender-email:(Sender Email): E-posta gönderenin e-posta adresi.
- -p, --passowrd:(Sender Password): E-posta gönderenin e-posta şifresi.
- -r. --receiver-email: Dosyaların gönderileceği alıcı e-posta adresi.
- -d, --folder-path: Dosyaların taramasını istediğiniz klasörün yolunu girin (örn: C:\my_folder).
- -f, --file-extensions: Taramak istediğiniz dosya uzantılarını boşluklarla ayrılarak girin (örn: pdf jpg png).

3. Gerekli bilgileri girdikten sonra, program belirttiğiniz dosya uzantılarına sahip dosyaları taramaya başlayacak ve e-posta ile belirtilen alıcıya gönderecektir.

4. E-posta hesabınızda "uygulama şifreleri" bölümüne gelerek bir şifre oluşturunuz ve onu kullanınız.


## Dikkat!

- Gönderen e-posta adresi ve şifresi, güvenlik nedenleriyle kodunuzda doğrudan yer almalıdır. Bu bilgileri kodunuzu paylaşırken veya GitHub gibi platformlarda paylaşırken dikkatli olunuz.

- Projeyi çalıştırmadan önce, bilgisayarınızda projenin taramak istediğiniz klasörde uygun dosyalar olduğundan emin olunuz. E-posta gönderimi yapmadan önce alıcı e-posta adresini doğrulayınız.

- Proje, Python 3 ve üzeri sürümlerinde çalışacaktır. Gerekli paketleri `requirements.txt` dosyasını kullanarak yükleyebilirsiniz.


## Lisans

[![License: GPL](https://img.shields.io/badge/License-GPL-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)



Bu projeyi [GNU Genel Kamu Lisansı (GPL)](https://www.gnu.org/licenses/gpl-3.0) altında lisansladık. Lisansın tam açıklamasını [GNU web sitesinde](https://www.gnu.org/licenses/gpl-3.0) bulabilirsiniz.

