"""Create tasks in Asana from emails in Gmail"""
from common.turosana.gmail_api import GmailAPI
from common.turosana.asana_api import AsanaAPI

from common.turosana.utils import get_tasks

def check_emails():
    """Get emails from Gmail"""
    gmail_client = GmailAPI()
    emails = gmail_client.get_emails()
    gmail_client.close_connection()
    return emails

def create_tasks(emails):
    """Create tasks in Asana"""
    asana_client = AsanaAPI()

    for email in emails:
        data = f"{email['html']}"
        tasks = get_tasks(data)

        if not tasks:
            continue

        for name, date in tasks:
            print(f"Creating task: {name} for {date}")
            asana_client.create_task(name=name, date=date)


def run():
    """Run the script"""
    emails = check_emails()
    if emails:
        create_tasks(emails)

if __name__ == "__main__":
    run()
