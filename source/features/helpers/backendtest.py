import unittest
from unittest.mock import patch, MagicMock
from crknScrapper import CrknExcelExtractor


class TestUpdateChecker(unittest.TestCase):

   @patch('crknScrapper.yaml.safe_load')
   @patch('crknScrapper.requests.get')
   @patch('crknScrapper.BeautifulSoup')
   @patch('builtins.open', new_callable=unittest.mock.mock_open)
   @patch('crknScrapper.yaml.dump')
   def test_extract_excel_links(self, mock_yaml_dump, mock_open, mock_beautifulsoup, mock_requests_get, mock_yaml_load):
        
        config_path = 'source/config/config.yaml'
        mock_config = {'link': 'http://example.com', 'excel_links': []}
        mock_open.return_value.__enter__.return_value.read.return_value = 'fake_yaml_content'
        mock_yaml_load.return_value = mock_config
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response
        mock_beautifulsoup.return_value.find_all.return_value = [{'href': 'file1.xlsx'}, {'href': 'file2.xlsx'}]

    
        extractor = CrknExcelExtractor(config_path)
        excel_links = extractor.extract_excel_links()

   
        mock_requests_get.assert_called_once_with('http://example.com')
        mock_beautifulsoup.assert_called_once_with(mock_response.content, 'html.parser')
        mock_yaml_dump.assert_called_once()

    
        self.assertEqual(excel_links, ['http://example.com/file1.xlsx', 'http://example.com/file2.xlsx'])
        self.assertIn('http://example.com/file1.xlsx', extractor.config['excel_links'])
        self.assertIn('http://example.com/file2.xlsx', extractor.config['excel_links'])


if __name__ == '__main__':
    unittest.main()