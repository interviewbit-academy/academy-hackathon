import os

from flask import Flask
from flask import request
from flask import render_template

<<<<<<< HEAD
=======
from flask import render_template

# our fake db
>>>>>>> upstream/master
todo_store = {}
todo_store['depo'] = ['Go for run', 'Listen Rock Music']
todo_store['shivang'] = ['Read book', 'Play Fifa', 'Drink Coffee']
todo_store['raj'] = ['Study', 'Brush']
todo_store['sanket'] = ['Sleep', 'Code']
todo_store['aagam'] = ['play cricket', 'have tea']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

<<<<<<< HEAD
    def get_todos_by_name(name):
        return select_todos(name)
=======
    def select_todos(name):
        global todo_store
        return todo_store[name]

    def insert_todo(name, todo):
        global todo_store
        current_todos = todo_store[name]
        current_todos.append(todo)
        todo_store[name] = current_todos
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
>>>>>>> upstream/master

    def select_todos(name):
        global todo_store
        return todo_store[name]

    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('---------')
        print(name)
        print('---------')

        person_todo_list = get_todos_by_name(name)
<<<<<<< HEAD
        # return todo_view(person_todo_list)
        return render_template('todo_view.html', todos=person_todo_list)

    def add_todo_by_name(name, todo):
        # call DB function
        add_todo(name, todo)
        return

    def add_todo(name, todo):
        global todo_store
        current_todo = todo_store[name]
        current_todo.append(todo)
=======
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=person_todo_list)

>>>>>>> upstream/master

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
<<<<<<< HEAD
        print(name)
        print(todo)
=======
>>>>>>> upstream/master
        add_todo_by_name(name, todo)
        return 'Added Successfully'

    return app

