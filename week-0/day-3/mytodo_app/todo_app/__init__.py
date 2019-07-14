import os
from flask import Flask
from flask import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dc',
        DATABASE=os.path.join(app.instance_path, 'todo_app.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import todo
    app.register_blueprint(todo.bp)

    return app