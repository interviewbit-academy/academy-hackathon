import os

from flask import Flask, request, render_template, redirect, url_for

from . import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.initialize_app_db(app)

    def select_todos(name):
        db1 = db.Database(app)
        data = db1.get_todo(name)
        print("Todos for", name, ": ", data)
        return data

    def insert_todo(name, todo):
        db1 = db.Database(app)
        db1.add_todo(name, todo)
        return

    def add_todo_by_name(name, todo):
        # call DB function
        insert_todo(name, todo)
        return

    def get_todos_by_name(name):
        return select_todos(name)

    @app.route('/')
    def index():
        return render_template('todo_view.html')

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
            return render_template('todo_view.html', todos=person_todo_list)

    @app.route('/add_todos', methods=['POST'])
    def add_todos():
        name = request.form.get('name')
        todo = request.form.get('todo')
        add_todo_by_name(name, todo)
        return redirect(url_for('todos', name=name))
        # return

    return app
