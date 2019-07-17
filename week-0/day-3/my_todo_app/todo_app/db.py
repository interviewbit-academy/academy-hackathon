import pymysql

def initialize_db_app(app):
    db1 = Database(app)
    db1.cur.execute("DROP TABLE IF EXISTS user")
    f = open("todo_app/schema.sql", "r")
    sqlCommands = f.read().split(';')
    db1.cur.execute("DROP TABLE IF EXISTS user")
    for command in sqlCommands:
        try:
            print("Executing: ", command)
            db1.cur.execute(command)
        except:
            print("Skipped: ", command)

    db1.con.commit()


class Database:
    def __init__(self, app):
        host = "localhost"
        user = "manjeet"
        password = "Manjeet@12345"
        db = "flask_app"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def get_todo(self, name):
        sql_get_query = """ SELECT todo from `user`
                          WHERE username = (%s)"""

        self.cur.execute(sql_get_query, (name))
        result = self.cur.fetchall()
        just = []
        for item in result:
            just.append(item['todo'])
        print("-----------------")
        print(just)
        print("-----------------")
        return just

    def add_todo(self, name, todo):
        sql_insert_query = """ INSERT INTO `user`
                          (`username`, `todo`) VALUES (%s,%s)"""
        print("Want to insert -> ", (name, todo))
        self.cur.execute(sql_insert_query, (name, todo))
        self.con.commit()
