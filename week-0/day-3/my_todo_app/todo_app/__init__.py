import os
from flask import Flask
from flask import request
from flask import render_template

todo_store = {}
todo_store['depo'] = ['Go for run', 'Listen Rock Music']
todo_store['raj'] = ['Study', 'Brush']
todo_store['shivang'] = ['Read book', 'Play Fifa', 'Drink Coffee']
todo_store['sanket'] = ['Sleep', 'Code']
todo_store['aagam'] = ['play cricket', 'have tea']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # MODEL
    def select_todos(name):
        #global todo_store
        return todo_store[name]
    
    def insert_todos(name,todo):
        get = todo_store[name]
        get.append(todo)
        todo_store[name] = get
        return 

    def add_todo_by_name(name,todo):
        #call to db function
        insert_todos(name,todo)
        return 
    
    def delete_todo_by_name(name,todo):
        #call to db function
        return
    
    def update_todo_by_name(name,todo):
        #call to db function
        return

    # # Connecting db
    # db.init_app(app)
    def get_todo_by_name(name):
        # database_connection = db.get_db()
        # data = database_connection.execute('select tasks from todo_ where username=?',(name,)).fetchall()
        # print(data)
        try:
            return select_todos(name)
        except:
            None
    
    # CONTROLLER
    # http://127.0.0.1:5000/todos?name=rohit
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        person_todo_list = get_todo_by_name(name) # Connect model and controller
        if person_todo_list == None:
            # throw 404 to user and browser
            return render_template('404.html'), 404
        #return view.todo_view(person_todo_list)   # Connect view and controller
        return render_template('todo_view.html',todos=person_todo_list)

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name,todo)
        return "Added sucessful"
    
    @app.route('/delete_todos')
    def delete_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        return "deleted sucessful"
    
    @app.route('/update_todos')
    def update_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        return "deleted sucessful"

    return app

