import os

from flask import Flask
from flask import request
from flask import render_template

todo_store={'raj':['Go for a run','Listen to Rock music'],
			'manmohan':['Study','Brush'],
			'shivang':['Read Book','Play Fifa']}
def create_app(test_config=None):
    # create and configure the app
	app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	def select_todos(name):
		global todos_store
		try:
			return todo_store[name]
		except:
			return None
	
	def get_todo_name(name):
		return select_todos(name)

	def insert_todo(name,todo):
		global todo_store
		current_todos=todo_store[name]
		current_todos.append(todo)
		todo_store[name]=current_todos

	def add_todo_by_name(name,todo):
		insert_todo(name,todo)

	@app.route('/todos')
	def todos():
		name=request.args.get('name')
		print('-----\n'+name+'\n-----')
		todos_acc_name=get_todo_name(name)
		if todos_acc_name==None:
			return render_template('404.html'),404
		else:
			return render_template('todo_view.html',todos=todos_acc_name)

	@app.route('/add_todos')
	def add_todos():
		name=request.args.get('name')
		todo=request.args.get('todo')
		print('------\n',request,name+'\n','------')
		add_todo_by_name(name,todo)
		return 'Added Successfully'

	@app.route('/delete_todos')
	def delete_todos():
		return 'Deleted Successfully'
	return app
