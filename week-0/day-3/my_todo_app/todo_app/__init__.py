import os

from flask import Flask
from flask import request

from flask import render_template
from flaskext.mysql import MySQL
mysql = MySQL()

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
# our fake db
todo_store = {}
todo_store['depo'] = ['Go for run', 'Listen Rock Music']
todo_store['shivang'] = ['Read book', 'Play Fifa', 'Drink Coffee']
todo_store['raj'] = ['Study', 'Brush']
todo_store['sanket'] = ['Sleep', 'Code']
todo_store['aagam'] = ['play cricket', 'have tea']

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'swapnil159'
app.config['MYSQL_DATABASE_DB'] = 'todo_app'
#app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'
mysql.init_app(app)

def select_todos(name):
    print('---------')
    print(name)
    print('---##----')
    cur = mysql.get_db().cursor()
    print('yu')
    cur.execute("SELECT todos FROM todo WHERE name = %s",(name,))
    todo_list = cur.fetchall()
    print(type(todo_list))
    return todo_list

def insert_todo(name, todo):
    global todo_store
    current_todos = todo_store[name]
    current_todos.append(todo)
    todo_store[name] = current_todos
    return

def add_todo_by_name(name, todo):
    # call DB function
    insert_todo(name, todo)
    return

def get_todos_by_name(name):
    print('---------')
    print(name)
    print('-----#---')
    return select_todos(name)



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


@app.route('/add_todos')
def add_todos():
    name = request.args.get('name')
    todo = request.args.get('todo')
    add_todo_by_name(name, todo)
    return 'Added Successfully'

if __name__ == '__main__':
    app.run()

