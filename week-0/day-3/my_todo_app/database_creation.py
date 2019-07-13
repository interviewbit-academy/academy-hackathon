import sqlite3

c= sqlite3.connect('database.db')
conn=c.cursor()
print("Opened database successfully")

create_names = "CREATE TABLE names (name TEXT)"
create_todos = "CREATE TABLE todos (name TEXT, todo TEXT, FOREIGN KEY (name) REFERENCES names(name) );"

conn.execute(create_names)
conn.execute(create_todos)
print("Table created successfully")


conn.execute('INSERT INTO names VALUES("Toufique")')
conn.execute('INSERT INTO names VALUES("Palash")')
conn.execute('INSERT INTO todos VALUES("Toufique", "eat")')
conn.execute('INSERT INTO todos VALUES("Toufique", "sleep")')
conn.execute('INSERT INTO todos VALUES("Toufique", "repeat")')
conn.execute('INSERT INTO todos VALUES("Palash", "fifa")')


c.commit()
c.close()
print("Records added successfully")