from helpers.search import search_title_substring, search_ISBN
db_p = 'source/storage/database/proj.db'
search_title_substring('bre', db_p)
search_ISBN('978', db_p)