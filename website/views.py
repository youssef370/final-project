from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from flask_login import login_required
from .models import User, Post
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    db_posts = Post.query.all()
    posts = [post for post in db_posts]
    return render_template('home.html', user=current_user, posts=posts)

@views.route('/new-post', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        post_text = request.form.get('post-text')
        post_title = request.form.get('post-title')

        print(User.query.filter_by())
        
        new_post = Post(title=post_title, text=post_text, likes=0 , dislikes=0)
        
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('views.home'))

    return render_template('new-post.html', user=current_user)

@views.route('/top-posts')
def top_posts():
    db_posts = Post.query.all()
    posts = [post for post in db_posts]
    return render_template('home.html', user=current_user, posts=posts)