setup_requirements:
	pip install -r requirements.txt
set_institution_db:
	python source/program/main_menu/helpers/download_excel.py
	python source/program/main_menu/helpers/parse_excel.py
	python source/program/main_menu/qtdropdown.py
search:
	python source/program/search_page/searching.py