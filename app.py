import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   return conn

def execute_sql(conn, sql):
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == '__main__':
         
   create_library_sql = """
   -- library table
   CREATE TABLE IF NOT EXISTS library (
      id integer PRIMARY KEY,
      Author text NOT NULL,
      Title text NOT NULL,
      Status bool,
    );
   """
   create_author_sql = """
   -- author table
   CREATE TABLE IF NOT EXISTS author (
       Author_ID integer PRIMARY KEY,
       Title text NOT NULL,
       Status bool,
       FOREIGN KEY (Author_ID) REFERENCES library(id) ON DELETE CASCADE
    );
   """
  
   db_file = "library.sqlite"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_library_sql)
       execute_sql(conn, create_author_sql)
       conn.close()