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
        the_view='List of my todos'+'<br/>'
        for todo in todos:
            the_view+=todo+'<br/>'
        the_view+='----The end of List-----'
        return the_view
    def get_todos_byname(name):
        if name=='rahul':
            return['Go for music','learn swimming']
        elif name=='shivang':
            return['speaking French','Learning to cook']
        elif name=='prashant':
            return['have to study','have to drink tea']
        else:
            return[]
    @app.route('/todos')
    def todos():
        name=request.args.get('name')
        print('---------------')
        print(name)
        print('---------------') 
        my_todos=[]
        todo_list=get_todos_byname(name)
        return todo_view(todo_list)
    # a simple page that list my todos
    return app

