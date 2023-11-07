"""Module to interact with the Gmail API"""
import imaplib
import email
import os

# Constants for Gmail access
EMAIL = os.environ.get('GMAIL_EMAIL')
PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
IMAP_SERVER = 'imap.gmail.com'

class GmailAPI:
    """Class to interact with the Gmail API"""
    def __init__(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(EMAIL, PASSWORD)

    def get_emails(self):
        """Get emails from Gmail"""
        emails = []
        # Select the "Turo" label
        status, _ = self.mail.select('"Turo"')  # Adjust the name if the label is different
        if status != 'OK':
            raise Exception("Could not select the 'Turo' mailbox. Check if the mailbox name is correct.")
            
        # Search for unseen emails from noreply@mail.turo.com
        status, messages = self.mail.search(None, '(UNSEEN FROM "noreply@mail.turo.com")')
        if status != 'OK':
            raise Exception("Could not search the mailbox. Check if the search syntax is correct.")
            
        for num in messages[0].split():
            status, data = self.mail.fetch(num, '(RFC822)')
            if status == 'OK':
                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)
                if email_message.is_multipart():
                    for part in email_message.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        if content_type == "text/html" and "attachment" not in content_disposition:
                            html_content = part.get_payload(decode=True).decode()
                            emails.append({'subject': email_message['subject'], 'html': html_content})
                            break
                else:
                    html_content = email_message.get_payload(decode=True).decode()
                    emails.append({'subject': email_message['subject'], 'html': html_content})
        return emails

    def close_connection(self):
        """Close the connection to the IMAP server"""
        self.mail.close()
        self.mail.logout()