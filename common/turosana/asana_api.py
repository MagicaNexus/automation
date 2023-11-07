"""Module to interact with the Asana API"""
import os
import requests
from requests.exceptions import RequestException


class AsanaAPI:
    """Class to interact with the Asana API"""
    def __init__(self):
        self.base_url = 'https://app.asana.com/api/1.0'
        asana_access_token = os.environ.get('ASANA_ACCESS_TOKEN')
        self.headers = {
            'Authorization': f'Bearer {asana_access_token}'
        }
    
    def create_task(self, name, date):
        """Create a task in Asana"""
        url = f"{self.base_url}/tasks"

        data = {
            'data': {
                'name': name,
                'due_at': date,
                'projects': [os.environ.get('ASANA_PROJECT_ID')],
                'assignee': os.environ.get('ASANA_USER_ID'),
                'assignee_section': os.environ.get('ASANA_SECTION_ID')
            }
        }
        try:
            response = requests.post(url, headers=self.headers, json=data, timeout=10)
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
            return response.json()
        except RequestException as e:
            print(f"An error occurred: {e}")