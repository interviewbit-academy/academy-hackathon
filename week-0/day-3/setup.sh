# create project directory
echo "creating project directory"
mkdir my_todo_app
cd my_todo_app

# we are using python 3
# setup python virtual environment
echo "setting up virtual environment"
python3 -m venv venv


# activate virtual environment
echo "activating virtual environment"
. venv/bin/activate

echo "virtual environment created successfully"

# install Flask
echo "install flask"
pip install Flask

echo "--- Flask Installed Successfully ---"

echo "create a flask app"
# make an flask app
mkdir todo_app

cd todo_app

touch __init__.py # __init__.py is just like main function in c/c++ program

# adding file content
echo "adding minimal code to run flask app"
cat > __init__.py << SERVER_SCRIPT
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
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

    return app

SERVER_SCRIPT

# going back to parent directory
cd ../

# setting up some environment variables
echo "setting up few environment variables"
export FLASK_APP=todo_app
export FLASK_ENV=development

# command to deactivate virtual environment
#deactivate
