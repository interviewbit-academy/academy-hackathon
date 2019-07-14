import os

from flask import Flask
from flask import request
from flask import render_template
from flask_mysqldb import MySQL

# todo_store={}
# todo_store['shivang']=['dddd','dssdsd','sgfdxaf']
# todo_store['rahul']=['asfda','asafa','sadad']
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='2020'
    app.config['MYSQL_DB']='todo'
    mysql=MySQL(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    def todo_view(todos):
        the_view='List of todos:'+'<br/>'
        for todo in todos:
            the_view+=(todo+'<br/>')
        the_view+='---List ends here----'
        return the_view




    def select_todos(name):
        # global todo_store
        # return todo_store[name]
        cur=mysql.connection.cursor()

        cur.execute("select todo from todos where name=%s",(name,))
        print('fdf')
        data=cur.fetchall()
        data1=[]
        for i in data :
            data1.append(i[0])
        return data1

    def get_todo_by_name(name):
        try:
            return select_todos(name)
        except:
            return None

    def add_todos1(name,todo):
        cur=mysql.connection.cursor()
        cur.execute("insert into todos (name ,todo) values(%s,%s)",(name,todo))
        mysql.connection.commit()
        cur.close()



    def add_todo_by_name(name,todo):
        #call db func

        add_todos1(name,todo)

    @app.route('/todos',methods=('GET','POST'))
    def todos():
        if request.method=='POST':
            name=request.form['name']

            cc=get_todo_by_name(name)
            # return todo_view(cc)
            if cc==None:
                return render_template('404.html'), 404
            else:
                return render_template('todo_view.html',todos=cc)

        return render_template('todo_query.html')




    @app.route('/add_todos',methods=('GET','POST'))
    def add_todos():
        if request.method=='POST':
            name=request.form['name']
            todo=request.form['todo']
            add_todo_by_name(name,todo)
            return 'added success'

        return render_template('add_todo.html')



    @app.route('/delete_todo')
    def delete_todo():
        return 'deleted todo'

    return app
