from flaskext.mysql import MySQL

f = open("todo_app/schema.sql","r")



def init_db(app):
    mysql = MySQL(app)

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'aman'
    app.config['MYSQL_DATABASE_DB'] = 'todo'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    #mysql.init_app()
    conn = mysql.connect()
    cursor =conn.cursor()
    #cursor.execute("DROP TABLE IF EXISTS user")
    sqlCommands = f.read().split(';')

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except :
            print("Skipped: ",command)
    conn.commit()
    return conn,cursor
