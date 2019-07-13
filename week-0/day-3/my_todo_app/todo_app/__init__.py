import os

from flask import Flask
from flask import request
from flask import render_template
import Model as model


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def get_todos_by_name(name):
        return model.select_todos(name)
    def add_todo_by_name(name,todo):
        model.insert_todo(name, todo)
        return 



    # http://127.0.0.1:5000/todos?name=duster

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name, todo)
        return 'Added Successfully'

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        person_todo_list = get_todos_by_name(name)
        if person_todo_list == None:
            return render_template('error.html')
        else:
            return render_template('todo_view.html',todos=person_todo_list)
    return app

