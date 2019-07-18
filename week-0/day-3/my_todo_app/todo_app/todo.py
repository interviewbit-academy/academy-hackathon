from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('todo', __name__)

from todo_app.extensions import mysql

def select_todos(name):
    cur = mysql.get_db().cursor()
    cur.execute("SELECT todos FROM todo WHERE name = %s",(name,))
    todo_list = cur.fetchall()
    return todo_list

def insert_todo(name, todo):
    print(name,todo)
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO todo (name, todos) VALUES (%s, %s)",(name,todo))
    conn.commit()
    cur.close()
    conn.close()
    return

def add_todo_by_name(name, todo):
    # call DB function
    insert_todo(name, todo)
    return

def get_todos_by_name(name):
    return select_todos(name)



# http://127.0.0.1:5000/todos?name=duster
@bp.route('/todos')
def todos():
    name = request.args.get('name')    
    person_todo_list = get_todos_by_name(name)
    if person_todo_list == None:
        return render_template('404.html'), 404
    else:
        return render_template('todo_view.html',todos=person_todo_list)


@bp.route('/add_todos')
def add_todos():
    name = request.args.get('name')
    todo = request.args.get('todo')
    add_todo_by_name(name, todo)
    return 'Added Successfully'