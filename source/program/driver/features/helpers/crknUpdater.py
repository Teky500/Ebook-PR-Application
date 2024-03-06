import time
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QPlainTextEdit
import requests
from bs4 import BeautifulSoup
import yaml
from urllib.parse import urljoin




class UpdateChecker:
    def __init__(self, config_path='source/config/config.yaml'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as config_file:
            return yaml.safe_load(config_file)

    def get_website_excel_files(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            base_url = response.url
            return [urljoin(url, a['href']) for a in soup.find_all('a', href=True) if a['href'].endswith('.xlsx')]
        else:
            print(f"Failed to fetch URL. Status code: {response.status_code}")
            return []

    def compare(self, new_excel_files):
        # Check if 'excel_files' key exists in the current configuration
        if 'excel_links' not in self.config:
            self.config['excel_links'] = []

        # Convert the lists of Excel files to sets for easier comparison
        current_files_set = set(self.config['excel_links'])
        new_files_set = set(new_excel_files)
        # Check for additions or removals in the sets
        added_files = new_files_set - current_files_set
        removed_files = current_files_set - new_files_set

        # Show the UI for user interaction regardless of changes
        return (added_files, removed_files)

    def update_config(self):
        self.config['excel_links'] = self.get_website_excel_files(self.config['link'])
        print('NEW CONFIG LINKS')
        print(self.config['excel_links'])
        with open(self.config_path, 'w') as config_file:
            yaml.dump(self.config, config_file)

if __name__ == "__main__":
    start = time.perf_counter()
    checker = UpdateChecker()
    url = checker.config.get('link')
    new_excel_files = checker.get_website_excel_files(url)
    (added, removed) = checker.compare(new_excel_files)
    end = time.perf_counter()
 
# find elapsed time in seconds
    ms = (end-start) 
    print(f"Elapsed {ms:.03f} secs.")

