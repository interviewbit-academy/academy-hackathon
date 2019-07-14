import os

from flask import Flask
from flask import request
from flask import render_template

todo_store = {}
todo_store['depo']= ['go for run','listen music']
todo_store['himesh']=['read book','lol']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos
    @app.route('/shivang')
    def shivang():
        return todo_view()

    @app.route('/todos')
    def todos():
        name=request.args.get('name')
        print(name)

        person_todo_list=select_todos(name)
        if person_todo_list == None:
            return 'Not found'
        return render_template('view.html',todos=person_todo_list)


    @app.route('/add_todos')

    def add_todos():
        name=request.args.get('name')
        todo=request.args.get('todo')
        print('---')
        print(name,todo)
        add_todos_by_name(name,todo)

        return 'added successfully'

    def get_todos_by_name(name):
        try:
            return select_todos(name)
        except:
            return None


    def add_todos(name,todo):
        global todo_store
        current_todos=todo_store[name]
        current_todos.append(todo)
        todo_store[name]=current_todos


    def add_todos_by_name(name,todo):
        add_todos(name,todo)


    def select_todos(name):
        global todo_store
        try:
            return todo_store[name]
        except:
            return None


    @app.route('/himesh')
    def himesh():
        return todo_view()

    def todo_view():
        return ('Wake Up' + '<br/>' +
            'Drink' + '<br/>' +
            'Read Non-fiction Novel' + '<br/>'
        )



    return app

