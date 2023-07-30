import os
import glob
import yagmail
import argparse
import signal
import sys

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

def signal_handler(sig, frame):
    print("\nTarama işlemi durduruldu.")
    sys.exit(0)

if __name__ == "__main__":
    # Ctrl+C tuş kombinasyonunu ele almak için signal sinyalini tanımlayalım
    signal.signal(signal.SIGINT, signal_handler)

    # Argümanları işlemek için argparse nesnesi oluşturalım
    parser = argparse.ArgumentParser(description="Bilgisayarınızdaki dosyaları e-postayla gönderin.")
    parser.add_argument("-s", "--sender-email", required=True, help="E-posta gönderenin e-posta adresi.")
    parser.add_argument("-p", "--sender-password", required=True, help="E-posta gönderenin e-posta şifresi.")
    parser.add_argument("-r", "--receiver-email", required=True, help="Dosyaların gönderileceği alıcı e-posta adresi.")
    parser.add_argument("-d", "--folder-path", required=True, help="Dosyaların taramasını istediğiniz klasörün yolunu girin (örn: C:\\my_folder).")
    parser.add_argument("-f", "--file-extensions", nargs="+", required=True,
                        help="Taramak istediğiniz dosya uzantılarını boşluklarla ayrılarak girin (örn: pdf jpg png)")

    args = parser.parse_args()

    # Belirtilen klasördeki dosyaları ve alt klasörlerdeki dosyaları tarayalım
    attachment_files = []
    for extension in args.file_extensions:
        attachment_files.extend(glob.glob(os.path.join(args.folder_path, f"**/*.{extension}"), recursive=True))

    # E-posta konusu ve içeriğini belirleyelim
    subject = "Dosyalarınız Ektedir"
    body = "İşte dosyalarınız."

    # E-posta gönderme işlemlerini tamamlayalım
    for attachment_file in attachment_files:
        # E-posta gönderme işlemini çağıralım
        send_email(args.sender_email, args.sender_password, args.receiver_email, subject, body, attachment_file)

    print("E-postalar gönderildi.")
