import os

from flask import Flask
from flask import request
from flask import redirect, url_for
from flask import render_template
import sqlite3 as sql




def create_app(test_config=None):

	'''conn = sql.connect("database.db")
	print('Opened database succesfully')
	conn.execute('CREATE TABLE todo_list_db (ID INTEGER PRIMARY KEY, NAME TEXT, TASK TEXT)')
	print('Table created succesfully')
	conn.close()'''

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
		cur.execute('SELECT ID, NAME, TASK FROM todo_list_db WHERE NAME LIKE "{goal}" '.\
			format(goal = name))

		rows = cur.fetchall()
		print('///')
		for row in rows:
			print(row[0])
		print('///')
		con.commit()
		
		return rows

	def insert_todos(name, todo):
		con = sql.connect("database.db")
		cur = con.cursor()

		cur.execute('INSERT INTO todo_list_db (NAME, TASK) VALUES (?, ?)', (name, todo))
		con.commit()
		print('Added succesfully')
		con.close()
		return

	def delete_todo(iden):
		con = sql.connect("database.db")
		cur = con.cursor()

		cur.execute('DELETE FROM todo_list_db WHERE ID={goal} '.\
			format(goal=iden))
		con.commit()
		print('Deleted')
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

	def delete_todo_by_id(iden):
		return delete_todo(iden)


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


	@app.route('/add_todos', methods=['POST'])
	def add_todos():
		name=request.form.get('user_name')
		todo=request.form.get('todo')
		add_todo_by_name(name, todo)
		return redirect(url_for('todos',name=name))

	@app.route('/delete_todos')
	def delete_todos():
		name=request.args.get('name')
		iden=request.args.get('iden')
		delete_todo_by_id(iden)
		return redirect(url_for('todos',name=name))


	return app

