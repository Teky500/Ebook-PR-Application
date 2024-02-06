CREATE TABLE books 
    (ISBN text PRIMARY KEY NOT NULL, 
    title text NOT NULL, 
    publisher text NOT NULL, 
    platform_yop int, 
    OCN int, 
    result text NOT NULL,
    spreadsheet text NOT NULL);
CREATE TABLE platforms 
    (spreadsheet text PRIMARY KEY,
    platform text NOT NULL);
