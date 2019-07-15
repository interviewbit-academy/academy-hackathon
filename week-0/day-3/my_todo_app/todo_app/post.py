from flask import(
    Blueprint, flash, g, redirect, render_template,request,url_for,session
)
from werkzeug.exceptions import abort

from todo_app.auth import login_required
from todo_app.db import get_db
from flask import session

bp=Blueprint('post',__name__)

@bp.route('/')
def index():
    user_id=session.get('user_id')
    print(user_id)
    if user_id is None:
        return redirect('auth/login')

    db=get_db()  
    posts = db.execute(
        'SELECT * FROM post WHERE author_id=?',(user_id,)

        # 'SELECT p.id, title, body, created, author_id'
        # 'FROM post p WHERE p.author_id=?', (user_id,)
    ).fetchall()
    return render_template('posts/index.html',posts=posts)


@bp.route('/create',methods=('GET','POST'))
@login_required
def create():
    if request.method=='POST':
        title=request.form['title']
        body=request.form['body']
        error=None

        if not title:
            error='Title required'
        if error is not None:
            flash(error)
        else:
            db=get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('post.index'))
    return render_template('posts/create.html')

def get_post(id,check_author=True):
    post=get_db().execute(
       'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404,"Post id {0} doesn't exist.".format(id))
    
    if check_author and post['author_id']!=g.user['id']:
        abort(403)
    
    return post

@bp.route('/<int:id>/update',methods=('GET','POST'))
@login_required
def update(id):
    post=get_post(id)

    if request.method=='POST':
        title=request.form['title']
        body=request.form['body']
        error=None

        if not title:
            error='Title is required'
        
        if error is not None:
            flash(error)
        else:
            db=get_db()
            db.execute(
                'UPDATE post SET title=?,body=?'
                'WHERE id=?'
                (title,body,id)
            )
            db.commit()
            return redirect(url_for('post.index'))
    
    return render_template('posts/update.html',post=post)

@bp.route('/<int:id>/delete',methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db=get_db()
    db.execute('DELETE FROM post WHERE id=?',(id,))
    db.commit()
    return redirect(url_for('post.index'))
