"""Utility functions for the TUROSANA project"""
import re

from datetime import datetime, timedelta
import locale
import pytz
from bs4 import BeautifulSoup, NavigableString, Tag

# Set the locale to French to interpret French month names
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

def get_date(date, delay=0):
    """Convert a date string to the desired format"""
    # Subtract 12 hours
    time = datetime.strptime(date, '%A %d %B %Y %H:%M') - timedelta(hours=delay)

     # Set the original timezone for the datetime object
    original_timezone = pytz.timezone('America/Montreal')
    localized_dt = original_timezone.localize(time)

    # Convert the localized datetime object to UTC
    utc_dt = localized_dt.astimezone(pytz.utc)

    # Format it into ISO 8601 format
    return utc_dt.strftime('%Y-%m-%dT%H:%M:00.000Z')


def get_tasks(html_content, word="Ka-ching!"):
    """Extract tasks from the HTML content of an email"""
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(string=lambda text: word in text)

    content = None
    price = None
    for element in elements:
        parent = element.parent
        if isinstance(parent, Tag):
            next_sibling = parent.find_next_sibling()

            while isinstance(next_sibling, NavigableString) or (next_sibling and not next_sibling.get_text(strip=True)):
                next_sibling = next_sibling.find_next_sibling()
            content = parent
            price = next_sibling
            break  # Assuming we only need the first match
    if not (content and price):
        return None

    content_str = str(content)
    price_str = str(price)

    # Extract various pieces of information using regex
    name_match = re.search(r'voyage de (\w+)', content_str)
    name = name_match.group(1) if name_match else "Unknown"

    d_match = re.search(r'du <strong>([^<]+)</strong>', content_str)
    d_date_str = d_match.group(1).strip() if d_match else None

    a_match = re.search(r'au <strong>(.+)</strong>', content_str)
    a_date_str = a_match.group(1) if a_match else None

    price_match = re.search(r'(\d+,\d{2}) \$', price_str)
    price = price_match.group(1).replace(',', '.') if price_match else "0"

    # Create titles using the extracted data
    b_title = f"🧽 Préparer la voiture TURO pour {name}"
    d_title = f"🟢 Départ TURO de {name} ({price}$)"
    a_title = f"🔴 Arrivée TURO de {name}"

    # Convert dates to the desired format if they were found
    departure = get_date(d_date_str) if d_date_str else "Unknown"
    arrival = get_date(a_date_str) if a_date_str else "Unknown"
    before = get_date(d_date_str, 12) if d_date_str else "Unknown"
    
    return [(b_title, before), (d_title, departure), (a_title, arrival)]