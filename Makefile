set_institution_db:
	python source/makePython/download_excel.py
	python source/makePython/parse_excel.py
	python source/makePython/add_to_database.py