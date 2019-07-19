import os

from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL

# our fake db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    conn,cursor = db.init_db(app)

    sql_insert_query = """INSERT INTO `user`
                          (`name`, `item`) VALUES (%s,%s)"""

    sql_get_query = """SELECT item FROM `user`
                          WHERE name = (%s)"""

    def select_todos(name):
        cursor.execute(sql_get_query,(name))
        data = cursor.fetchall()
        list = []
        for d in data:
            list.append(d[0])
        #conn.close()
        return list

    def insert_todo(name,todo):
        cursor.execute(sql_insert_query,(name,todo))
        conn.commit()
        #conn.close()
        return

    def add_todo_by_name(name, todo):
        # call DB function
        insert_todo(name, todo)
        return

    def get_todos_by_name(name):
        try:
            return select_todos(name)
        except:
            return None


    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('---------')
        print(name)
        print('---------')

        person_todo_list = get_todos_by_name(name)
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=person_todo_list)


    @app.route('/add_todos', methods=['GET','POST'])
    def add_todos():
        if request.method == 'POST':
            name = request.form.get('name')
            todo = request.form.get('todo')
            print("{},{}".format(name,todo))
            add_todo_by_name(name, todo)
            print("working")
        return "added sucessfuly"


    return app
