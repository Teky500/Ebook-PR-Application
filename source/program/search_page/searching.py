from helpers.search import search_title_substring, search_ISBN, search_OCN
db_p = 'source/storage/database/proj.db'
print("TITLE SEARCH RESULTS")
search_title_substring('Big', db_p)
print("ISBN SEARCH RESULTS")
search_ISBN('978', db_p)
print("OCN SEARCH RESULTS")
search_OCN(51970502, db_p)