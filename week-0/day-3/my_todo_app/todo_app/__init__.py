import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    def todo_view(todos):
        v='my todo'+'<br>'
        for todo in todos:
            v=v+(todo+'<br>')
        return v;
    def get_todos_by_name(name):
        if name=='depo':
            return ['run','run']
    # a simple page that list my todos
    @app.route('/todo')
    def todo():
        name=request.args.get('name')
        p=get_todos_by_name(name)
        return todo_view(p)


    return app

