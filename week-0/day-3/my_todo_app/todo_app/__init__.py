import os

from flask import Flask
from flask import request
from flask import render_template
todo_store = {}
todo_store['rahul']=['Go for music','learn swimming','yes']
todo_store['prashant']=['have to study','have to drink tea','yes']
todo_store['depo']=['have to study','have to drink coffee','yes']
todo_store['sanjay']=['have to study economics','have to drink coffee','yes']
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    def todo_view(todos):
        the_view='List of my todos'+'<br/>'
        for todo in todos:
            the_view+=todo+'<br/>'
        the_view+='----The end of List-----'
        return the_view
    def select_todos(name):
        global todo_store
        return todo_store[name]
    def get_todos_byname(name):
        try:
            return select_todos(name)
        except:
            return None
    def insert_todos(name,todo):
        global todo_store
        current_todos=todo_store[name]
        current_todos.append(todo)
        todo_store[name]=current_todos
        return
    def add_todo_byname(name,todo):
        insert_todos(name,todo)
        #call DB function
        return
    '''def get_todos_byname(name):
        if name=='rahul':
            return
        elif name=='shivang':
            return['speaking French','Learning to cook','yes']
        elif name=='prashant':
            return['have to study','have to drink tea','yes']
        else:
            return[]'''
    @app.route('/todos')
    def todos():
        name=request.args.get('name')
        num=(int)(request.args.get('num'))
        print('---------------')
        print(name)
        print('---------------') 
        my_todos=[]
        full_todo_list=get_todos_byname(name)
        if(full_todo_list==None):
            return render_template ('404.html'),404
        else:
            half_todo_list=full_todo_list[0:num]
        #return todo_view(half_todo_list)
            return render_template ('todo_view.html', todos=half_todo_list)
    
            # a simple page that list my todos
    @app.route('/add_todos')
    def add_todos():    #this todos are not persistent as it will work as static data
        name=request.args.get('name')
        todo=request.args.get('todo')
        add_todo_byname(name,todo)
        print('-----------')
        print(name,todo)
        print('-----------')
        return 'Added Successfully'
    return app

