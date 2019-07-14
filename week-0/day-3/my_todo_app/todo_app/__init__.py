import os
from flask import Flask,request,current_app, render_template,redirect,url_for
from flaskext.mysql import MySQL



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #Getting cursor and conn object from db.py
    from . import db
    cursor,conn = db.init_db(app)

    sql_insert_query = """ INSERT INTO `user`
                          (`username`, `todo`) VALUES (%s,%s)"""
    sql_get_query = """ SELECT todo from `user`
                          WHERE username = (%s)"""
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        # cursor.execute("SELECT todo from user where username='" + name + "'")
        cursor.execute(sql_get_query,(name))
        data = cursor.fetchall()
        just = []
        for i in data:
            just.append(i[0])
        print("Todos for",name,": ",just)
        return just

    def insert_todo(name, todo):
        print("Want to insert",name,todo)
        cursor.execute(sql_insert_query,(name,todo))
        conn.commit()
        return

    def add_todo_by_name(name, todo):
        # call DB function
        insert_todo(name, todo)
        return

    def get_todos_by_name(name):
        return select_todos(name)

    @app.route('/todos')
    def todos():
        name = request.args.get('name')

        person_todo_list = get_todos_by_name(name)
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('index.html',todos=person_todo_list,flag = 1)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/add')
    def add_t():
        return render_template('add_todo.html')

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name, todo)
        return render_template('add_todo.html',name=name,todo=todo)
        # return redirect(url_for('add_t'))
    return app