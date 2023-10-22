from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import current_user
from flask_login import login_required
from .models import User, Post, Like
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    db_posts = db.session.execute(db.select(Post)).scalars()
    posts = [post for post in db_posts]
    return render_template('home.html', user=current_user, posts=posts)

@views.route('/new-post', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        post_text = request.form.get('post-text')
        post_title = request.form.get('post-title')
        
        new_post = Post(title=post_title, text=post_text, user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('views.home'))

    return render_template('new-post.html', user=current_user)

@views.route('/top-posts')
def top_posts():
    db_posts = db.session.execute(db.select(Post).order_by(Post.likes)).scalars()
    posts = [post for post in db_posts]
    return render_template('home.html', user=current_user, posts=posts)

@views.route('/my-posts')
@login_required
def my_posts():
    my_page = True
    db_posts = db.session.execute(db.select(Post).filter(Post.user_id == current_user.id)).scalars()
    posts = [post for post in db_posts]
    return render_template('home.html', user=current_user, posts=posts, my_page=my_page)

@views.route('/delete-post', methods = ['POST'])
@login_required
def delete_post():
    post_id = request.form.get('id')
    deleted_post = db.session.execute(db.select(Post).filter(Post.id == post_id)).scalar()

    db.session.delete(deleted_post)
    db.session.commit()

    return redirect(url_for('views.my_posts'))

@views.route("/like-post/<post_id>", methods=['POST'])
@login_required
def like(post_id):
    post = db.session.execute(db.select(Post).filter(Post.id == post_id)).scalar()
    like = db.session.execute(db.select(Like).filter(Like.user_id == current_user.id, Like.post_id == post_id)).scalar()
    
    
    if not post:
        return jsonify({'error': 'Post doesn\'t exist'}, 400)
    elif like:
        db.session.delete(like)
        post.likes -= 1
        isLiked = False # The like button isn't clicked yet
    else:
        like = Like(user_id=current_user.id, post_id=post.id)
        db.session.add(like)
        post.likes += 1
        isLiked = True # The like button got clicked
    
    db.session.commit()
    
    return jsonify({'likes': post.likes, 'liked': isLiked})