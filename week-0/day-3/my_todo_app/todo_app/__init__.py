from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

#Config db
db  = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        #fetch data
        userDetails = request.form
        name = userDetails['name']
        return view(name)
    
    return render_template('index.html')

@app.route('/addtodo',methods=['GET','POST'])
def addtodo():
    if request.method == 'POST':
        det = request.form
        name = request.args.get('name')
        li = det['todo']

        cur = mysql.connection.cursor()
        todolist = cur.execute("SELECT list FROM todoapp where name = '"+name+"'")
        if todolist>0:
            list = cur.fetchall()
            a = list[0][0].split(',')
        cur.close()

        cur = mysql.connection.cursor()
        li = list[0][0]+','+li
        print ("----" + li + "----")
        cur.execute("UPDATE todoapp SET list = '"+li+"' WHERE name = '"+name+"'")
        mysql.connection.commit()
        cur.close()

        print ("Todo Added")
        return view(name)

@app.route('/view')
def view(name):
    cur = mysql.connection.cursor()
    todolist = cur.execute("SELECT list FROM todoapp where name = '"+name+"'")
    if todolist>0:
        list = cur.fetchall()
        a = list[0][0].split(',')
        return render_template('view.html',user=name,list=a)
    else:
        return ("NO DATA FOUND")

@app.route('/delete')
def delete():
    i = request.args.get('index')
    i = int(i)
    name = request.args.get('name')

    cur = mysql.connection.cursor()
    todolist = cur.execute("SELECT list FROM todoapp where name = '"+name+"'")
    if todolist>0:
        list = cur.fetchall()
        a = list[0][0].split(',')
    cur.close()
    del(a[i])
    li=','.join(a)
    cur = mysql.connection.cursor()
    cur.execute("UPDATE todoapp SET list = '"+li+"' WHERE name = '"+name+"'")
    mysql.connection.commit()
    cur.close()
    return view(name)

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method == 'POST':
        i = request.args.get('index')
        i = int(i)
        name = request.args.get('name')
        det = request.form
        updated = det['upded']
        print (updated)
        cur = mysql.connection.cursor()
        todolist = cur.execute("SELECT list FROM todoapp where name = '"+name+"'")
        if todolist>0:
            list = cur.fetchall()
            a = list[0][0].split(',')
        cur.close()

        a[i]=updated
        li=','.join(a)
        cur = mysql.connection.cursor()
        cur.execute("UPDATE todoapp SET list = '"+li+"' WHERE name = '"+name+"'")
        mysql.connection.commit()
        cur.close()
        return view(name)



if __name__ == '__main__':
    app.run(debug=True)
