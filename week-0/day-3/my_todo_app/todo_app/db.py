from flaskext.mysql import MySQL
# import os
# print(os.getcwd())
f = open("todo_app/schema.sql","r")
# print(f.read())

def init_db(app):
    mysql = MySQL()
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'manjeet'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'Manjeet@12345'
    app.config['MYSQL_DATABASE_DB'] = 'flask_app'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)
    conn = mysql.connect()
    cursor =conn.cursor()

    sqlCommands = f.read().split(';')

    for command in sqlCommands:
        try:
            # print(command)
            cursor.execute(command)
        except :
            print("Skipped: ",command)
    conn.commit()
    return cursor,conn