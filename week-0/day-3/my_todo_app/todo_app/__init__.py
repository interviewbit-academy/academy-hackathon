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
            the_view += (todo + '<br/>')

        the_view += ('--list end here--')
        return the_view

    def get_todo_by_name(name):
        my_todos = []
        if name =='ayush':
            my_todos = ['walk','music','drink_coffee'] 
        elif name =='shivang':
            my_todos = ['walk','music','drink_coffee'] 
        elif name =='raj':
            my_todos = ['walk','music','drink_coffee'] 
        elif name =='depo':
            my_todos = ['walk','music','drink_coffee'] 
        elif name == 'sanket':
            my_todos = ['sleep','eat']
        else:
            my_todos = []
        return my_todos

    @app.route('/todos')
    def todos():
        #http://127.0.0.1:5000/todos?name=ayush
        name = request.args.get('name')
        print('-----server log---------')
        print(name)
        print('-------------------------')
        
        my_todos = get_todo_by_name(name)
        
        return todo_view(my_todos)
    
    return app

