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
        the_view='List of my todos:'+ '<br/>'
        for todo in todos:
            the_view +=(todo + '<br/>')
        the_view +='----LIST ENDS HERE----'
        return the_view
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        if name=='akash':
            my_todos=['cricket','music','sleeping']
        elif name=='karthik':
            my_todos=['crying','playing','eating']
        elif name=='lakshaya':
            my_todos=['playing','laughing','eating']
        else:
            my_todos=[]
        return todo_view(my_todos)

    return app

