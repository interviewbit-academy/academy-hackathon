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

    todolist = {'aayush':['Wake Up','Drink Coffee','Sleep'],'shivang':['Wake Up','Drink Coffee','Read Non-fiction Novel']}

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print(name)
        if name in todolist:
        	return todo_view(todolist[name])
        else:
                return todo_view([])

    def todo_view(todlist):
        the_view = '<h1> List of my todos: </h1>' + '<br/>'
        for todo in todlist:
                 the_view+= (todo + '<br/>')
        the_view+='----- LIST ENDS HERE -----'
        return the_view
	
    @app.route('/shivang')
    def shivang():
        mytodo = ['Wake Up','Drink Coffee','Read Non-fiction Novel']
        return todo_view(mytodo)
	
    @app.route('/aayush')
    def aayush():
        mytodo = ['Wake Up','Drink Coffee','Sleep']
        return todo_view(mytodo)


    return app

