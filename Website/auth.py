from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():  # put application's code here
    return 'login'

@auth.route('/sign-up')
def signup():  # put application's code here
    return 'sign-up'


@auth.route('/sign-out')
def logout():  # put application's code here
    return 'sign-out'

