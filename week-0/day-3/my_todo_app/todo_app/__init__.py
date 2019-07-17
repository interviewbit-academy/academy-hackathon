import os

from flask import Flask
from flask import request
from flask import render_template
from flaskext.mysql import MySQL


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'
	app.config['MYSQL_DATABASE_USER'] = 'administrator'
	app.config['MYSQL_DATABASE_PASSWORD'] = '12345678!@#QWEqwe'
	app.config['MYSQL_DATABASE_DB'] = 'tododb'
	mysql = MySQL(app)
	mysql.init_app(app)
	
	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	
	#MODEL STRATS HERE

	def get_from_db(name):
		conn=mysql.connect()
		cur=conn.cursor()
		cur.execute("SELECT work FROM todolisttable WHERE name = %s",(name))
		data=cur.fetchall()
		data1=[A[0] for A in data]
		conn.commit()
		if len(data1) == 0 :
			return None
		return data1


	def get_todos_by_name(name):
		try:
			return get_from_db(name)
		except:
			return None
	
	def add_in_list(name,work):
		conn=mysql.connect()
		cur = conn.cursor()
		cur.execute("INSERT INTO todolisttable(name, work) VALUES (%s, %s)", (name, work))
		conn.commit()
		#mysql.connection.commit()
		#cur.close()
		return 

	def verify_before_add(name,work):
		return add_in_list(name,work)

	#MODELS ENDS HERE
	
	#...............................................................................................................#


	#CONTROLLER STARTS HERE
	

	@app.route('/add_todo')
	def add_todo():
		name=request.args.get('name')
		work=request.args.get('work')
		verify_before_add(name,work)
		return 'ADDED SUCCESFULLY'


	# a simple page that list my todos
	@app.route('/todos')
	def todos():
		name = request.args.get('name')
		dolist = get_todos_by_name(name)
		if dolist!=None :
			return render_template('todo_view.html',worklist = dolist)
		else :
			return render_template('404.html'),404
	#...................................................................................................................#		

	return app

