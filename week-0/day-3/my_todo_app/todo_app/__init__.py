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

    from . import db
    db.init_app(app)


    def get_todos_by_name(name):
        database = db.get_db()
        cursor = database.execute('SELECT tasks FROM todo WHERE name=?',(name,)).fetchall()
        if cursor == None:
            return []
        todos = []
        for val in cursor:
            print(val['tasks'])
            todos.append(val['tasks'])
        
        return todos
        


    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        num = request.args.get('num')
        num=int(num)
        print('---------')
        print(name,num)
        print('---------')

        person_todo_list = get_todos_by_name(name)

        from . import view
        return view.todo_view(person_todo_list[:num])

    
    return app

