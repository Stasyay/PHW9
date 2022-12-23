import sqlite3
from sqlite3 import Error
from pathlib import Path

file_name = "telephone_directory.sqlite"
relative_file_directory = Path(file_name)

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as massage:
        print(f"The error '{massage}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as massage:
        print(f"The error '{massage}' occurred")

create_people_table = """
CREATE TABLE IF NOT EXISTS people (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT(30) NOT NULL,
  surname TEXT(30) NOT NULL
);
"""

create_phone_numbers_table = """
CREATE TABLE IF NOT EXISTS phones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  phone_number INTEGER(9) NOT NULL,
  people_id INTEGER NOT NULL,
  FOREIGN KEY (people_id) REFERENCES people(id)
);
"""

connection = create_connection(relative_file_directory)

execute_query(connection, create_people_table)

execute_query(connection, create_phone_numbers_table)

create_data_for_people_table = """
INSERT INTO
  people (name, surname)
VALUES
  ('Fedor1', 'Sannikov1'),
  ('Fedor2', 'Sannikov2'),
  ('Fedor3', 'Sannikov3'),
  ('Fedor4', 'Sannikov4'),
  ('Fedor5', 'Sannikov5');
"""

create_data_for_phone_numbers_table = """
INSERT INTO
  phones (phone_number, people_id)
VALUES
  (620070, 1),
  (620071, 1),
  (620072, 2),
  (620073, 3),
  (620074, 4),
  (620075, 5);
"""

execute_query(connection, create_data_for_people_table)

execute_query(connection, create_data_for_phone_numbers_table)