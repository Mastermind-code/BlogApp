from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'post':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("password is incorrect", category='error')
        else:
            flash("email is incorrect", category="error")

    return render_template("login.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        username_exists = User.query.filter_by(username=username).first()
        email_exists = User.query.filter_by(email=email).first()

        if email_exists:
            flash("email is used please try another email", category='error')
        elif username_exists:
            flash('username already exists. Please try another username', category='error')
        elif len(username) < 4:
            flash('username is too short please try another.', category='error')
        elif len(email) < 4:
            flash('email is too short please try another.', category='error')
        elif len(password) < 6:
            flash('password is too short please try another.', category='error')
        elif password != password_confirm:
            flash('password don\'t match, please try another.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password, method='sha256'), email=email)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("signup successful", category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html")


@auth.route('/sign-out')
def logout():
    logout_user()
    return redirect(url_for("views.home"))
