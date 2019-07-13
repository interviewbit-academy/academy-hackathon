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
            ls = "".join(list(fetch_data)).split(",")
            cur.close()
            return ls
        except:
            return None
    
    def commit_in_dB(todo_ls,name):
        val = ",".join(todo_ls)
        cur = mysql.connection.cursor()
        cur.execute("UPDATE todo_list SET list_of_todo=%s WHERE name LIKE %s", [val,name] )
        mysql.connection.commit()
        cur.close()

    def add_todo_by_name(name,todo):
        ls = get_todo_by_name(name)
        ls.append(todo)
        commit_in_dB(ls,name)
        print(ls)
        return 
    
    def delete_todo_by_name(name,todo):
        ls = get_todo_by_name(name)
        try:
            index = ls.index(todo)
            del ls[index]
            commit_in_dB(ls,name)
            print(ls)
        except:
            return
    
    def update_todo_by_name(name,todo,update_todo):
        ls = get_todo_by_name(name)
        try:
            index = ls.index(todo)
            ls[index] = update_todo
            commit_in_dB(ls,name)
            print(ls)
        except:
            return

    # CONTROLLER
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html')

    def todo_list(name):
        person_todo_list = get_todo_by_name(name) # Connect model and controller
        if person_todo_list == None:
            # throw 404 to user and browser i.e syntax render_template('404.html'), 404
            return render_template('404.html'), 404
        return render_template('todo_view.html',name=name,todos=person_todo_list) # Connect view and controller
    
    # CURD
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        return todo_list(name)

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        print("------------------")
        add_todo_by_name(name,todo)
        print("Added Sucessfully")
        print("------------------")
        return todo_list(name)
    
    @app.route('/delete_todos')
    def delete_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        print("------------------")
        delete_todo_by_name(name,todo)
        print("Deleted Sucessfully")
        print("------------------")
        return todo_list(name)
    
    @app.route('/update_todos')
    def update_todos():
        name = request.args.get('name')
        todo = request.args.get('old')
        update_todo = request.args.get('new')
        print("------------------")
        update_todo_by_name(name,todo,update_todo)
        print("Updated Sucessful")
        print("------------------")
        return todo_list(name)

    return app

