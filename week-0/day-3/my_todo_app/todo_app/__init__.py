import os
from flask import Flask
from flask import request
from flask import render_template
from flask_mysqldb import MySQL

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'todo'
    mysql = MySQL(app)


    # MODEL
    def get_todo_by_name(name):
        try:
            cur = mysql.connection.cursor()
            cur.execute( "SELECT list_of_todo FROM todo_list WHERE name LIKE %s", [name] )
            fetch_data = cur.fetchone()#fetchall()
            # print("----------------------")
            ls = "".join(list(fetch_data)).split(",")
            return ls
            # print(ls)
            # print("----------------------")
        except:
            return None
    
    def insert_todos(name,todo):
        # get = todo_store[name]
        # get.append(todo)
        # todo_store[name] = get
        return 
    
    def delete_todos(name,todo):
        return 
    
    def update_todos(name,todo):
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

    # CONTROLLER
    # http://127.0.0.1:5000/todos?name=rohit&todo=dummy
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        person_todo_list = get_todo_by_name(name) # Connect model and controller
        if person_todo_list == None:
            # throw 404 to user and browser i.e syntax render_template('404.html'), 404
            return render_template('404.html'), 404
        return render_template('todo_view.html',name=name,todos=person_todo_list) # Connect view and controller

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
        return "update sucessful"

    return app

