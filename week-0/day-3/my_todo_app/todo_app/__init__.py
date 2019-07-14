import os

from flask import Flask
from flask import request 
from flask import render_template

todo_store ={}
todo_store['akash']= ['cricket','music','sleeping']
todo_store['karthik']= ['crying','playing','eating']
todo_store['lakshaya']= ['playing','laughing','eating']
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    def select_todos(name):
        global todo_store
        return todo_store[name]
    def insert_todos(name,todo):
        global todo_store
        current_todos = todo_store[name]
        current_todos.append(todo)
        todo_store[name] = current_todos
        return
    def add_todo_by_name(name,todo):
        add_todos(name,todo)
    def get_todos_by_name(name):
        try:
            return select_todos(name)
        except:
            return None
    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        insert_todos(name,todo)
        return "added successfully"
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        my_todos=get_todos_by_name(name)
        if my_todos==None:
            return render_template('404.html'),404
        else:
            return render_template('todo_view.html',todos=my_todos)

    return app

