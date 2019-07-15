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
    def todo_view(my_todos):
        the_view='List of ToDos:'+'<br/>'
        for todo in my_todos:
            the_view+=(todo+'<br/>')
        the_view+='-----LIST ENDS HERE----'
        return the_view
        # return (
        #     'List of ToDos:'+'<br/>'+
        #     'Wake Up' + '<br/>' +
        #     'Drink Coffee' + '<br/>' +
        #     'Read Non-fiction Novel' + '<br/>'+
        #     '-----LIST ENDS HERE----'
        # )
    # a simple page that list my todos
    @app.route('/saurabh')
    def saurabh():
        todo=['wake Up','Lunch','Time Pass','Sleep']
        return todo_view(todo)

    @app.route('/shivang')
    def shivang():
        todo=['Wake Up','Drink Coffee','Study','Sleep']
        return todo_view(todo)
    return app

