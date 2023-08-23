from flask import Blueprint, render_template, request
from flask_login import current_user
from flask_login import login_required
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/new-post', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        pass
    return render_template('new-post.html', user=current_user)
