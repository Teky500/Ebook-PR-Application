# Ebook-PR-Application

The goal of this application is to allow librarians to access and know whether they have perpetual rights to a specific book.
This is done by scraping excel files from the CRKN Website (using this test page to get the files from, https://library.upei.ca/test-page-ebooks-perpetual-access-project). These excel files are then added to a local SQLite database, and functionalities such as searching for a specific book, or manually upload excel files to the database are created, and a neat front-end GUI to support user usage is designed.

# Setup
For development: do `pip install -r requirements.txt`, then run the mainrun.py file. Make sure you have Python 3.12 installed.

For production: run the mainrun.exe in the dist folder.

