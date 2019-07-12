import os

from flask import Flask
from flask import request
from flask import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    from . import db
    db.init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Welcome to TODOS List !!'

    def get_todos_by_name(name,num):
        dbc = db.get_db()
        user=dbc.execute(
            'SELECT task FROM list WHERE name = ?', (name,)
        ).fetchone()
        if user==None:
            return 'No user found'
        todo_list=[]
        print(user)
        for task in user:
            todo_list=task
        todo_list=todo_list.split(',')

        if num!=None:
            num=int(num)
            todo_list=todo_list[0:num]
        return todo_list


    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        num = request.args.get('num')

        person_todo_list = get_todos_by_name(name,num)
        return render_template('todo_view.html',todos=person_todo_list)


    return app