import os

from flask import Flask,flash,session,redirect
from flask import request,url_for
import pymysql
from flask import render_template

def connect():
    con = pymysql.connect(host = "localhost",user = "root" ,password="",db = "todo_app",
                          cursorclass = pymysql.cursors.DictCursor)
    cur = con.cursor()

    return cur,con

# todo_store = {}
# todo_store['depo'] = ['Go for run', 'Listen Rock Music']
# todo_store['shivang'] = ['Read book', 'Play Fifa', 'Drink Coffee']
# todo_store['raj'] = ['Study', 'Brush']
# todo_store['sanket'] = ['Sleep', 'Code']
# todo_store['aagam'] = ['play cricket', 'have tea']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "super secret key"

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        try:
            cursor,con = connect()
            x = cursor.execute("select todo from todo_list where username = (%s)",(name))
            data = cursor.fetchall()
            print(data)

            cursor.close()
            con.close()
            return data
        except Exception as e:
            print(str(e))

    def insert_todo(name, todo):
        try:
            cursor,con = connect()
            print(name,todo)
            cursor.execute("insert into todo_list(username,todo) values(%s,%s)",(name,todo))
            con.commit()
            cursor.close()
            con.close()
        except Exception as e:
            print(str(e))


        return

    def add_todo_by_name(name, todo):
        # call DB function
        insert_todo(name, todo)
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
        print('---------')
        print(name)
        print('---------')

        person_todo_list = get_todos_by_name(name)
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=person_todo_list)


    @app.route('/add_todo/',methods = ['GET','POST'])
    def add_todo():
        name = request.values.get('username')
        todo = request.values.get('todo')
        print(name,todo)
        add_todo_by_name(name, todo)
        flash('Added Successfully')
        return render_template('todo_view.html')

    @app.route('/db_check/')
    def check_db():
        try:
            cursor,con = connect()
            return 'Done'
        except Exception as e:
            return (str(e))


    @app.route('/dashboard/')
    def dashboard():
        return render_template('todo_view.html') 


    @app.route('/see_todo/',methods = ['GET','POST'])
    def get_page():
        name = request.values.get('username')
        print(name)
        session['username'] = name
        return render_template('view_list.html',todos = get_todos_by_name(name))

    @app.route('/delete_todo/',methods = ['GET','POST'])
    def delete_todo():
        todo = request.form.get('delete')
        print(todo)
        name = session['username']
        try:
            cursor,con = connect()
            cursor.execute("Delete from todo_list where username = (%s) and todo = (%s) LIMIT 1",(name,todo))
            con.commit()
            cursor.close()
            con.close()
            return render_template('view_list.html',todos = get_todos_by_name(name))
        except Exception as e:
            print(str(e))

    @app.route('/update_todo/',methods = ['GET','POST'])
    def update_todo():
        new_todo = request.form.get('todo')
        todo = request.form.get('update')
        print(todo)
        name = session['username']
        try:
            cursor,con = connect()
            cursor.execute("Update todo_list set todo = (%s) where username = (%s) and todo = (%s) LIMIT 1",(new_todo,name,todo))
            con.commit()
            cursor.close()
            con.close()
            return render_template('view_list.html',todos = get_todos_by_name(name))
        except Exception as e:
            print(str(e))
    return app

