import os

from flask import Flask
from flask import request

from flask import render_template


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


    def select_todos(name):
        database = db.get_db()
        cursor = database.execute('SELECT tasks FROM todo WHERE name=?',(name,)).fetchall()
        if cursor == None:
            return []
        todos = []
        for val in cursor:
            print(val['tasks'])
            todos.append(val['tasks'])

        return todos

    def insert_todos(name, todo):
        database = db.get_db()
        database.execute('INSERT INTO todo (name, tasks) VALUES (?,?)',(name, todo))
        database.commit()
        return

    def delete_todo_from_db(name, todo):
        database = db.get_db()
        database.execute('DELETE FROM todo WHERE name=? AND tasks=?',(name, todo))
        database.commit()
        return

    def update_todo_in_db(name, todo, updatedTodo):
        database = db.get_db()
        database.execute('UPDATE todo SET tasks=? WHERE name=? AND tasks=?',(updatedTodo, name, todo))
        database.commit()
        return

    def add_todo_by_name(name,todo):
        insert_todos(name, todo)
        return

    def delete_todos_by_name(name, todo):
        delete_todo_from_db(name, todo)
        return

    def update_todos_by_name(name, todo, updatedTodo):
        update_todo_in_db(name, todo, updatedTodo)
        return

    def get_todos_by_name(name):
        try:
            return select_todos(name)
        except:
            return None

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
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=person_todo_list[:num])

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        print('------')
        print(name, todo)
        print('------')
        add_todo_by_name(name,todo)
        return 'Added successfully!!'

    @app.route('/delete_todos')
    def delete_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        print('------')
        print(name, todo)
        print('------')
        delete_todos_by_name(name, todo)
        return 'deleted successfully'

    @app.route('/update_todos')
    def update_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        updatedTodo = request.args.get('update')
        print('------')
        print(name, todo, updatedTodo)
        print('------')
        update_todos_by_name(name, todo, updatedTodo)
        return 'updated successfully'

    return app
