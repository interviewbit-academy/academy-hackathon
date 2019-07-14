import os

from flask import Flask
from flask import request

from flask import render_template
from flaskext.mysql import MySQL  


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    mysql = MySQL()
 
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'ayush'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
    app.config['MYSQL_DATABASE_DB'] = 'mydb'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("SELECT * from user where name= %s",name)
        data = cursor.fetchone()
        return(data[2])

    def insert_todo(name, todo):
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT into user(name,todo) values (%s,%s)",(name,todo))
        conn.commit()
        return

    def add_todo_by_name(name, todo):
        # call DB function
        insert_todo(name, todo)
        return

    def get_todos_by_name(name):
        return select_todos(name)


    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('---------')
        print(name)
        print('---------')
        person_todo_list = get_todos_by_name(name)
        todo=person_todo_list.split(',')
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=todo)

    @app.route('/todos_by_num')
    def todos_by_num():
        name = request.args.get('name')
        num=request.args.get('num')
        num=int(num)
        print('---------')
        print(name)
        print(type(num))
        print('---------')
        person_todo_list = get_todos_by_name(name)
        todo=person_todo_list.split(',')
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=todo[:num])

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name, todo)
        return 'Added Successfully'

    return app

