from flask import Blueprint

config = Blueprint('config', __name__)

@config.route('/login')
def login() :
    return "<p>Login</p>"

@config.route('/logout')
def logout() :
    return "<p>Logout</p>"

@config.route('/sign-up')
def sign_up() :
    return "<p>Sign Up</p>"