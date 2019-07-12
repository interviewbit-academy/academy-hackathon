import os
from flask import Flask
from flask import request
from flask import render_template
# from . import view,db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # # Connecting db
    # db.init_app(app)

    # MODEL
    def get_todo_by_name(name,num):
        # database_connection = db.get_db()
        # data = database_connection.execute('select tasks from todo_ where username=?',(name,)).fetchall()
        # print(data)
        if name == 'depo':
            todo =  ['Go for run', 'Listen Rock Music']
        elif name == 'shivang':
            todo = ['Read book', 'Play Fifa', 'Drink Coffee']
        elif name == 'raj':
            todo = ['Study', 'Brush']
        elif name == 'sanket':
            todo = ['Sleep', 'Code']
        elif name == 'aagam':
            todo = ['play cricket', 'have tea']
        else:
            todo = []
        return todo[:int(num)]
    
    # CONTROLLER
    # http://127.0.0.1:5000/todos?name=rohit
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        num = request.args.get('num')
        # it will print in server terminal
        print('---------')
        print(name)
        print('---------')
        person_todo_list = get_todo_by_name(name,num) # Connect model and controller
        #return view.todo_view(person_todo_list)   # Connect view and controller
        return render_template('todo_view.html',todos=person_todo_list,num=2)

    return app

