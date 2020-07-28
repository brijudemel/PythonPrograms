import sqlite3
def connect(dbname):
  con=sqlite3.connect(dbname)
  con.execute("CREATE TABLE IF NOT EXISTS QUOTES_TABLE (QUOTE TEXT , AUTHOR TEXT)")
  print("Table created Successfully!")
  con.close()

def insert(dbname,values):
  con=sqlite3.connect(dbname)
  con.execute("INSERT INTO QUOTES_TABLE (QUOTE,AUTHOR) VALUES (?,?)",values)
  con.commit()
  con.close()

def get_info(dbname):
  con=sqlite3.connect(dbname)
  cur=con.cursor()
  cur.execute("SELECT * FROM QUOTES_TABLE")
  table_data=cur.fetchall()
  for record in table_data:
    print(record)
  con.close()
def author_quotes(dbname,author):
  con=sqlite3.connect(dbname)
  cur=con.cursor()
  cur.execute("SELECT QUOTE FROM QUOTES_TABLE WHERE AUTHOR=(?)",author)
  table_data=cur.fetchall()
  for record in table_data:
    print(record)
  con.close()
