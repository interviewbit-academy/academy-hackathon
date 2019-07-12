import functools

from flask import (
    Blueprint, flash,g, redirect, render_template, request, session, url_for
)

from .db import get_db

bp = Blueprint('todo_view',__name__, url_prefix ='/')


def todo_list(todos):
    the_view = 'List of my todos: '+ '<br/>'
    for todo in todos:
        the_view += todo+'<br/>'
    the_view += '------LIST ENDS HERE--------'
    return the_view

def get_todos_by_name(name):
    if name == 'saurav':
        my_todo = ['go for shoping', 'study']
    elif name=='shivang':
        my_todo = ['go for run', 'start computer']
    elif name=='agrawal':
        my_todo = ['go for walk', 'start laptop']
    else:
        my_todo =[]
    return my_todo

@bp.route('/todo')
def todos():
    name = request.args.get('name')
    num = int(request.args.get('num'))
    print('*******************************')
    print(name)
    print(type(num))
    print('*******************************')
    person_todo_list = get_todos_by_name(name)
    person_todo_list_sublist = person_todo_list[:num]
    return todo_list(person_todo_list_sublist)
