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

    # a simple page that list my todos
    def get_todos_by_name(name):
        if name=='raj':
            return ['Eat','Sleep','Repeat']
        elif name=='shivang':
            return ['Brush','Study']
        elif name=='manish':
            return ['sleep','code']
        else:
            return []

    @app.route('/todos')
    def todos():
        name=request.args.get('name')
        print('------')
        print(name)
        print('------')

        todo_l=get_todos_by_name(name)
        return todo_view(todo_l)

    def todo_view(todos):
        the_view = 'List of my todos:' + '<br/>'
        for todo in todos:
            the_view += ( todo + '<br/>' )

        the_view += '---LIST ENDS HERE---'
        return the_view

    return app
