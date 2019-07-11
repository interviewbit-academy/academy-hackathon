import os

from flask import Flask
from flask import request

#local host http://127.0.0.1:5000/todos?name=user_name

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def todo_view(todos):
        the_view = '<h1>List of my Todos : </h1></br> '
        
        for i in todos:
            the_view += i + '</br>'
        
        the_view += '</br>------List ends here------'
        return the_view

    def get_todos_by_name(name):
        if name == 'amit':
            return ["competitive programming", "tv series", "nodejs", "flask"]
        elif name == 'raj':
            return ["catching a running train for no reason", "finding love", "being single"]
        elif name == 'shivang':
            return ["wakeup late", "teaching ib students basics of git", "drink coffee", "repeat"]
        else:
            return []
        

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('-------------')
        print(name)
        print('-------------')

        person_todo_list = get_todos_by_name(name)    

        return todo_view(person_todo_list)


    return app

