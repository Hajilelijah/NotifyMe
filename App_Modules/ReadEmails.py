import imaplib
import email
import json
import io


class Config:
    def __init__(self):
        with open("App_Configs\\ReadEmails.config.json", 'r') as file:
            config = json.load(file)

        self.EmailConfig = config["EmailConfig"]
        self.Server = self.EmailConfig["Server"]
        self.Port = self.EmailConfig["Port"]
        self.Username = self.EmailConfig["Username"]
        self.Password = self.EmailConfig["Password"]
        self.Sender = self.EmailConfig["Sender"]
        self.Receiver = self.EmailConfig["Receiver"]
        self.Message = config["Message"]
        self.Subject = self.Message["Subject"]
        self.Header = self.Message["Header"]
        self.Footer = self.Message["Footer"]


class get_Email:
    def process_emails():
        config = Config()

        # Connect to the IMAP server
        server = imaplib.IMAP4_SSL(config.Server, config.Port)
        server.login(config.Username, config.Password)

        try:
            # Select the folder to process (e.g., 'INBOX')
            folder = 'INBOX'
            server.select(folder)

            # Search for all emails in the selected folder
            _, message_numbers = server.search(None, 'ALL')
            message_numbers = message_numbers[0].split()

            # Loop through all messages
            for num in message_numbers:
                # Fetch the email object
                _, msg_data = server.fetch(num, '(RFC822)')
                email_obj = email.message_from_bytes(msg_data[0][1])

                # Print the subject of the email
                print("Subject:", email_obj['Subject'])

                # Print the body of the email
                body = ""
                if email_obj.is_multipart():
                    for part in email_obj.walk():
                        content_type = part.get_content_type()
                        if content_type == 'text/plain' or content_type == 'text/html':
                            body += part.get_payload(decode=True).decode()
                else:
                    body = email_obj.get_payload(decode=True).decode()

                print("Body:", body)
                print("----------")

        finally:
            # Close the connection to the IMAP server
            server.logout()

    def process_latest_email():
        config = Config()

        # Connect to the IMAP server
        server = imaplib.IMAP4_SSL(config.Server, config.Port)
        server.login(config.Username, config.Password)

        try:
            # Select the folder to process (e.g., 'INBOX')
            folder = 'INBOX'
            server.select(folder)

            # Search for all emails in the selected folder and sort them in reverse order
            _, message_numbers = server.search(None, 'ALL')
            message_numbers = sorted(message_numbers[0].split(), reverse=True)

            # Get the latest email (first in the list)
            latest_email_number = message_numbers[0]

            # Fetch the latest email object
            _, msg_data = server.fetch(latest_email_number, '(RFC822)')
            email_obj = email.message_from_bytes(msg_data[0][1])

            # Print the subject of the latest email
            print("Subject:", email_obj['Subject'])

            # Print the body of the latest email
            body = ""
            if email_obj.is_multipart():
                for part in email_obj.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain' or content_type == 'text/html':
                        body += part.get_payload(decode=True).decode()
            else:
                body = email_obj.get_payload(decode=True).decode()

            return body

        finally:
            # Close the connection to the IMAP server
            server.logout()

    def process_latest_email_subject():
        config = Config()

        # Connect to the IMAP server
        server = imaplib.IMAP4_SSL(config.Server, config.Port)
        server.login(config.Username, config.Password)

        try:
            # Select the folder to process (e.g., 'INBOX')
            folder = 'INBOX'
            server.select(folder)

            # Search for all emails in the selected folder and sort them in reverse order
            _, message_numbers = server.search(None, 'UNSEEN')
            message_numbers = sorted(message_numbers[0].split(), reverse=True)
            # print("Message Numbers:", message_numbers)

            # Print the selected folder
            selected_folder = server.select(folder)
            # print("Selected Folder:", selected_folder)

            # Get the latest email (first in the list)
            latest_email_number = message_numbers[0]

            # Fetch only the headers of the latest email
            _, msg_data = server.fetch(latest_email_number, '(BODY[HEADER])')
            email_headers = email.message_from_bytes(msg_data[0][1])

            # Get the subject from the headers
            subject = email_headers.get('Subject', '')

            _, msg_data = server.fetch(latest_email_number, '(RFC822)')
            email_obj = email.message_from_bytes(msg_data[0][1])

            # Check for attachments
            for part in email_obj.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    # Read the contents of the text file directly from the email attachment
                    file_contents = part.get_payload(decode=True).decode()

            # Print the subject of the latest email
            return str(subject), str(file_contents)

        finally:
            # Close the connection to the IMAP server
            server.logout()

    def process_latest_email_attachment():
        config = Config()

        # Connect to the IMAP server
        server = imaplib.IMAP4_SSL(config.Server, config.Port)
        server.login(config.Username, config.Password)

        try:
            # Select the folder to process (e.g., 'INBOX')
            folder = 'INBOX'
            server.select(folder)

            # Search for all emails in the selected folder and sort them in reverse order
            _, message_numbers = server.search(None, 'UNSEEN')
            message_numbers = sorted(message_numbers[0].split(), reverse=True)

            # Get the latest email (first in the list)
            latest_email_number = message_numbers[0]

            # Fetch the latest email object
            _, msg_data = server.fetch(latest_email_number, '(RFC822)')
            email_obj = email.message_from_bytes(msg_data[0][1])

            # Check for attachments
            for part in email_obj.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    # Read the contents of the text file directly from the email attachment
                    file_contents = part.get_payload(decode=True).decode()

                    return str(file_contents)

                    # You can further process the content of the text file here if needed

        finally:
            # Close the connection to the IMAP server
            server.logout()


# if __name__ == "__main__":
#     # get_Email.process_emails()
#     print(get_Email.process_latest_email_subject())
