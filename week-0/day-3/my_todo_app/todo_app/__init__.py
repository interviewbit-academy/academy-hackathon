import os

from flask import Flask
from flask import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='ska',
        DATABASE=os.path.join(app.instance_path, 'todo_app.sqlite')
    )
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos
    # def todo_list(todos):
    #     the_view = 'List of my todos: '+ '<br/>'
    #     for todo in todos:
    #         the_view += todo+'<br/>'
    #     the_view += '------LIST ENDS HERE--------'
    #     return the_view
    #
    # def get_todos_by_name(name):
    #     if name == 'saurav':
    #         my_todo = ['go for shoping', 'study']
    #     elif name=='shivang':
    #         my_todo = ['go for run', 'start computer']
    #     elif name=='agrawal':
    #         my_todo = ['go for walk', 'start laptop']
    #     else:
    #         my_todo =[]
    #     return my_todo

    # @app.route('/todo')
    # def todos():
    #     name = request.args.get('name')
    #     print(name)
    #     person_todo_list = get_todos_by_name(name)
    #     return todo_list(person_todo_list)

    from . import db
    db.init_app(app)

    from . import todo_view
    app.register_blueprint(todo_view.bp)
    return app
