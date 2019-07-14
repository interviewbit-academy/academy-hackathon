import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from todo_app.db import get_db

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        todolist = request.form['todolist']
        db = get_db()
        error = None 

        if not username:
            error = 'Username is required.'
        elif not todolist:
            error = 'A list is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, list) VALUES (?, ?)', (username, todolist)
            )
            db.commit()
            return redirect(url_for('todo.query')) 

        flash(error)

    return render_template('todo/register.html')

@bp.route('/query', methods=('GET', 'POST'))
def query():
    if request.method == 'POST':
        username = request.form['username']
        lsize = request.form['listsize']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif lsize is None:
            error = 'A size is required.'
        elif lsize is '0':
        	error = 'Please enter a value greater than 0.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            # uid = session['user_id']
            return redirect(url_for('todo.index', size=lsize))

        flash(error)

    return render_template('todo/query.html')

@bp.route('/index/<size>', methods=('GET', 'POST'))
def index(size):
    db = get_db()
    posts = db.execute(
        'SELECT list FROM user u WHERE id = u.id '
        # ' ORDER BY created DESC'
    ).fetchall()

    for row in posts: 
    	dolist = row['list']

    li = dolist.split(',')
    li_len = len(li)
    lsize = int(size)

    if lsize>=li_len:
    	return render_template('blog/index.html', size=size, posts=li)
    else:
    	i=0
    	x = []
    	for a in li:
    		x.append(a)
    		i = i + 1
    		if i>=int(size):
    			break
    return render_template('blog/index.html', size=size, posts=x)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/clearq')
def clearq():
    session.clear()
    return redirect(url_for('todo.register'))
