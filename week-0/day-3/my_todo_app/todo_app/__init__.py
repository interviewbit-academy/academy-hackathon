import os

from flask import Flask
from flask import request
from flask import render_template
import sqlite3 as sql




def create_app(test_config=None):

	#conn = sql.connect("database.db")
	#print('Opened database succesfully')
	#conn.execute('CREATE TABLE todo_list_db (NAME TEXT, TASK TEXT)')
	#print('Table created succesfully')
	#conn.close()

    # create and configure the app
	app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
	try:
	    os.makedirs(app.instance_path)
	except OSError:
	    pass


	def select_todos(name):
		con = sql.connect("database.db")
		
		print(name)
		
		cur = con.cursor()
		cur.execute('SELECT * FROM todo_list_db WHERE NAME LIKE "{goal}" '.\
			format(goal = name))

		#rows = cur.fetchall()
		print(cur)
		con.commit()
		
		return cur

	def insert_todos(name, todo):
			con = sql.connect("database.db")
			cur = con.cursor()

			cur.execute('INSERT INTO todo_list_db (NAME, TASK) VALUES (?, ?)', (name, todo))
			con.commit()
			print('Added succesfully')
			con.close()
			return



	def add_todo_by_name(name, todo):
		#call db
		return insert_todos(name, todo)


	def get_todos_by_name(name):
		try:
			return select_todos(name)
		except:
			None



	@app.route('/todos')
	def todos():
		name=request.args.get('name')
		print('----------')
		print(name)
		print('----------')
		my_todo=get_todos_by_name(name)

		if my_todo == None:
			return render_template('404.html'), 404
		else:
			return render_template('todo_view.html',todos=my_todo)


	@app.route('/add_todos')
	def add_todos():
		name=request.args.get('name')
		todo=request.args.get('todo')
		add_todo_by_name(name, todo)
		return ('Added succesfully')


	return app

