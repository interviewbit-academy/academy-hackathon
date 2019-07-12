import os

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for

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

    @app.route("/")
    def index():
        return "Welcome to TODO app <br/> pass name as request parameter to view todo <br/> and optional num to restrict list"

    def get_todos_by_name(name,num):
        dbc = db.get_db()
        cursor = dbc.execute('select todo from todo where username=?',(name,)).fetchone()
        if cursor==None:
            return ['NO SUCH USER']
        todo_list = []
        for row in cursor:
            todo_list = row
        todo_list = todo_list.split(',')

        if num!=None:
            try:
                num=int(num)
                todo_list=todo_list[0:num]
            except:
                pass            
        
        return todo_list

    @app.route('/todos')
    def todos():
        name=request.args.get('name')
        num=request.args.get('num')
        person_todos = get_todos_by_name(name,num)
        # return todo_view(person_todos)
        return render_template('todo_view.html',todos=person_todos)

    return app

