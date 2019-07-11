import os

from flask import Flask, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos

    def todo(todo):
        ans = ""
        for do in todo:
            ans = ans + " " + do + "<br>"
        return ans

    def get_todo_by_name(name):
        if name == 'shreyans':
            my_todo = ['Go for run', 'Sleep']
        elif name == 'raj':
            my_todo = ['Listen to music', 'Do coding']
        elif name == 'depo':
            my_todo = ['Build Application', 'Fuck']
        else:
            my_todo = ['User not registered']

        return my_todo

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('--------------------')
        print(name)
        print('--------------------')

        return todo(get_todo_by_name(name))

    return app
