import sqlite3
from sqlite3 import Error
from pathlib import Path

file_name = "database_logger.sqlite"
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
CREATE TABLE IF NOT EXISTS log_command (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data_and_time_message TEXT(30) NOT NULL,
  user_first_name TEXT(30) NOT NULL,
  user_id INTEGER(9) NOT NULL,
  user_message_text TEXT(200)
);
"""

connection = create_connection(relative_file_directory)

execute_query(connection, create_people_table)