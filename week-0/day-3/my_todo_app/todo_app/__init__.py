import os

from flask import Flask, request, render_template, redirect, url_for

todo_store = {}
todo_store['shreyans'] = ['Go for run', 'Sleep']
todo_store['raj'] = ['Listen to music', 'Do coding']
todo_store['depo'] = ['Build Application', 'Criket']

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

    # a simple page that list my todos
    #model
    def get_todo_by_name(name):
        return todo_store[name]

    #controller
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('--------------------')
        print(name)
        print('--------------------')

        #return todo_view(get_todo_by_name(name))
        return render_template('todo_view.html', todos=get_todo_by_name(name))

    @app.route('/addTodo', methods=['POST'])
    def add_todo():
        name = request.form.get('name')
        todo = request.form.get('todo')
        print('-------------------')
        print(name, todo)
        print('-------------------')
        if name not in todo_store:
            todo_store[name] = []
        if todo not in todo_store[name]:
            todo_store[name].append(todo)
        return "Success"

    return app
