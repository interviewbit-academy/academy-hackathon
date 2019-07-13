# commands to create databse.

import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

drop_table_names = "DROP TABLE IF EXISTS names;"
drop_tables_todos = "DROP TABLE IF EXISTS todos;"
create_names = "CREATE TABLE names (name TEXT)"
create_todos = "CREATE TABLE todos (name TEXT, todo TEXT, FOREIGN KEY (name) REFERENCES names(name) );";

conn.execute(drop_table_names);
conn.execute(drop_tables_todos);
conn.execute(create_names);
conn.execute(create_todos);
print("Table created successfully")


conn.execute('INSERT INTO names VALUES("rushit")');
conn.execute('INSERT INTO names VALUES("jasani")');
conn.execute('INSERT INTO names VALUES("hi")');
conn.execute('INSERT INTO todos(name, todo) VALUES("rushit", "todo 1")');
conn.execute('INSERT INTO todos(name, todo) VALUES("rushit", "todo 2")');
conn.execute('INSERT INTO todos(name, todo) VALUES("rushit", "todo 3")');
conn.execute('INSERT INTO todos(name, todo) VALUES("jasani", "todo 1")');
conn.execute('INSERT INTO todos(name, todo) VALUES("jasani", "todo 2")');
conn.execute('INSERT INTO todos(name, todo) VALUES("jasani", "todo 3")');
conn.execute('INSERT INTO todos(name, todo) VALUES("jasani", "todo 4")');
conn.execute('INSERT INTO todos(name, todo) VALUES("jasani", "todo 5")');

conn.commit();
print("Records added successfully");

conn.close()