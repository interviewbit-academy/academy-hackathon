import os

from flask import Flask
from flask import request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    todolist = {
        "aman" : ['Read','teach','sleep'],
        "shivang" : ['think','do nothing'],
        "raj" : ['think','do nothing'],
        "ujj" : ['think','do nothing','play']
    }
    def todoview(mytodos):
        view='list of my todos'+'<br/>'
        for todos in mytodos:
            view+=todos+'<br/>'
        view+='todos ends here'
        return (view)


    @app.route('/todos')
    def todos():
        name=request.args.get('name');
        print(name);
        if name in todolist:
            mytodos=todolist[name];
        else:
            mytodos=[];
        return todoview(mytodos)

    # a simple page that list my todos
    @app.route('/shivang')
    def shivang():
        mytodos=['Read','teach','sleep']
        return todoview(mytodos)
    @app.route('/aman')
    def aman():
        mytodos=['think','do nothing']
        return todoview(mytodos)
    
    return app

