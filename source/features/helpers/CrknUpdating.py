import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QPlainTextEdit
import requests
from bs4 import BeautifulSoup
import yaml
from urllib.parse import urljoin
import logging



class UpdateChecker:
    def __init__(self, config_path='source/config/config.yaml'):
        self.config_path = config_path
        self.config = self.loadConfig()

    def loadConfig(self):
        with open(self.config_path, 'r') as config_file:
            return yaml.safe_load(config_file)

    def getWebsiteExcelFiles(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                base_url = response.url
                return [urljoin(url, a['href']) for a in soup.find_all('a', href=True) if a['href'].endswith('.xlsx')]
            else:
                logging.info(f"Failed to fetch URL. Status code: {response.status_code}")
                return []
        except Exception as E:
            logging.info(E)
            logging.info('Could not fetch links. Are you connected to the internet?')
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

    def updateConfig(self):
        self.config['excel_links'] = self.getWebsiteExcelFiles(self.config['link'])
        logging.info('NEW CONFIG LINKS')
        logging.info(self.config['excel_links'])
        with open(self.config_path, 'w') as config_file:
            yaml.dump(self.config, config_file)

