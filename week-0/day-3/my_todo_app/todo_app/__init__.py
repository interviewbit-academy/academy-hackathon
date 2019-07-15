import os
from flask import Flask
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # ensure the instance folder exists
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'todo_app.sqlite')
    )


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that list my todos
    @app.route('/shivang')
    def shivang():
        return ('Wake Up' + '<br/>' +
            'Drink Coffee' + '<br/>' +
            'Read Non-fiction Novel' + '<br/>'
        )

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import post
    app.register_blueprint(post.bp)
    app.add_url_rule('/', endpoint='index')

    return app
