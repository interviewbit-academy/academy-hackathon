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
	
	def todo_view(todos):
		the_view=''
		for todo in todos:
			the_view+=todo+'<br>'
		return the_view
	
	def get_todo_name(name):
		dic={'raj':['Go for a run','Listen to Rock music'],
			'manmohan':['Study','Brush'],
			'shivang':['Read Book','Play Fifa']}
		try:
			return dic[name]
		except:
			return ''
	@app.route('/todos')
	def todos():
		name=request.args.get('name')
		print('-----\n'+name+'\n-----')
		return todo_view(get_todo_name(name))

	return app
