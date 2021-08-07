import sqlite3
def connect():
    conn=sqlite3.connect('db2.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dbb (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()
def insert(title,author,year,isbn):
    conn=sqlite3.connect('db2.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO dbb VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
def view():
    conn=sqlite3.connect('db2.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM dbb")
    rows=cur.fetchall()
    conn.close()
    return rows
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect('db2.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM dbb WHERE title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    conn.commit
    conn.close()
def update(id,title,author,year,isbn):
    conn=sqlite3.connect('db2.db')
    cur=conn.cursor()
    cur.execute("UPDATE dbb SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit
    conn.close()
def delete(id):
    conn=sqlite3.connect("db2.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM dbb WHERE id=?",(id,))
    conn.commit()
    conn.close()
connect()
print(view())
case=1
while(case>0):
    print("Enter the option to be selected:")
    print("0.Exit 1.View 2.Insert 3.Update 4.Delete")
    case=int(input())
    if(case==1):
        print(view())
    elif(case==2):
        title=input("Title: ")
        author=input("Author: ")
        year=int(input("Year: "))
        isbn=int(input("Isbn: "))
        insert(title,author,year,isbn)
    elif(case==3):    
        id=int(input("ID: "))
        title=input("Title: ")
        author=input("Author: ")
        year=int(input("Year: "))
        isbn=int(input("Isbn: "))
        update(id,title,author,year,isbn)
    elif(case==4):
    	id=int(input("ID: "))
    	delete(id)
    
