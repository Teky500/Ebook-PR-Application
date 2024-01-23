# Ebook-PR-Application

The goal of this application is to allow librarians to access and know whether they have perpetual rights to a specific book.
This is done by scraping excel files from the CRKN Website (using this test page to get the files from, https://library.upei.ca/test-page-ebooks-perpetual-access-project). These excel files are then added to a local SQLite database, and functionalities such as searching for a specific book, or manually upload excel files to the database are created, and a neat front-end GUI to support user usage is designed.

# Setup
Set up by using ```pip install -r requirements.txt```, to download the required packages to your current environment, alternatively, run the ```setup.bat``` file in the setup folder to install requirements on Windows.

# Running
Currently, there is a brief prototype functionality to add records to the database based on the institution. After installing the requirements, run ```make set_institution_db``` to download spreadsheet, set the database and insert records on linux, or use the ```run.bat``` file on Windows. 