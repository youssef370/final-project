from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Wrong passowrd', category='error')
        else:
            flash('Username doesn\'t exist', category='error')
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":

        # Get all the information from the sign up form
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password-confirm')

        # Query relevant info from the database
        user_email = User.query.filter_by(email=email).first()
        user_name = User.query.filter_by(username=username).first()

        # Check if the username exists, isn't taken, same for email, and if passwords match
        if user_name:
            flash('Username already taken', category='error')
        elif user_email:
            flash('Email already used', category='error')
        elif len(username) < 4:
            flash('Username must be greater than 4 characters. UsernameError', category='error')
        elif password != password_confirm:
            flash('Passwords don\'t match', category='error')
        # Add email validation
        else:

            # Create new user and add him to db
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')

            # Log the user in automatically
            login_user(new_user, remember=True)

            return redirect(url_for('views.home'))

    return render_template('sign-up.html', user=current_user)
