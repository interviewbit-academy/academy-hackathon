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
    	view = 'List starts here' + '<br/>'
    	for i in todos:
    		view += (i + '<br/>')
    	view += '---List ends here---'
    	return view

    def get_todos_by_name(name):
    	if name == 'abhi':
    		return ['Eat', 'sleep', 'code']
    	elif name == 'shivang':
    		return ['Eat', 'sleep']
    	else:
    		return  []



    @app.route('/todos')
    def todos():
    	name=request.args.get('name')
    	print('----------')
    	print(name)
    	print('----------')
    	my_todo=get_todos_by_name(name)
    	return todo_view(my_todo)

    return app

