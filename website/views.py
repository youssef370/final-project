from flask import Blueprint, render_template, request
from flask_login import current_user
from flask_login import login_required
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
        post = request.form.get('post-text')
        post_title = request.form.get('post-title')

    return render_template('new-post.html', user=current_user)
