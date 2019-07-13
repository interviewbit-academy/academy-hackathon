import os

from flask import Flask
from flask import request

from flask import render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    
    def select_todos(name,num):
        dbc = db.get_db()
        todo_list = []
        cursor = dbc.execute('SELECT todo FROM todo_table WHERE username=? LIMIT (?)',(name,num)).fetchall()
        if cursor is None:
            return None
        elif name is None:
            return None
        elif num is None:
            return None
        for row in cursor:
            todo_list.append(row['todo'])
        return todo_list

    def insert_todo(name, todo):
        dbc = db.get_db()
        error = None

        if not name:
            error = 'Username not found'
        elif not todo:
            error = 'Todo not found'

        if error is None:
            dbc.execute('INSERT INTO todo_table (username,todo) VALUES (?,?)',(name,todo))
            dbc.commit()
            return

    def add_todo_by_name(name, todo):
        insert_todo(name, todo)
        return

    def get_todos_by_name(name,num):
        try:
            return select_todos(name,num)
        except:
            return None

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        num = request.args.get('num')
        person_todo_list = get_todos_by_name(name,num)
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=person_todo_list)


    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name, todo)
        return 'Added Successfully'

    return app
