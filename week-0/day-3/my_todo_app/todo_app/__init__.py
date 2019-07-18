import os

from flask import Flask
from flask import request

from flask import render_template
from todo_app.extensions import mysql

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'swapnil159'
    app.config['MYSQL_DATABASE_DB'] = 'todo_app'
    #app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'
    mysql.init_app(app)

    from . import todo
    app.register_blueprint(todo.bp)

    return app

