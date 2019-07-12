import os

from flask import Flask
from flask import request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def todo_view(todos):
        the_view = 'List of my todos:' + '<br/>'
        for todo in todos:
            the_view += ( todo + '<br/>' )

        the_view += '---- LIST ENDS HERE ---'
        return the_view

    def get_todos_by_name(name,num):
        n=int(num)
        if name == 'depo':
            todo=['Go for run', 'Listen Rock Music']
            return todo[0:n]
        elif name == 'shivang':
            todo=['Read book', 'Play Fifa', 'Drink Coffee']
            return todo[0:n]
        elif name == 'raj':
            todo=['Study', 'Brush']
            return todo[0:n]
        elif name == 'sanket':
            todo=['Sleep', 'Code']
            return todo[0:n]
        elif name == 'Glen':
            todo=['Eat', 'have tea']
            return todo[0:n]
        else:
            return []


    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        num = request.args.get('num')
        print('---------')
        print(name)
        print('---------')

        person_todo_list = get_todos_by_name(name,num)
        return todo_view(person_todo_list)


    return app