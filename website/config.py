from flask import Blueprint, render_template, request, flash

config = Blueprint('config', __name__)

@config.route('/login', methods=['GET', 'POST'])
def login() :
    return render_template("login.html")

@config.route('/logout')
def logout() :
    return "<h1>Logout<h1>"

@config.route('/sign-up', methods=['GET', 'POST'])
def sign_up() :
    if request.method == 'POST' :
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 2:
            flash('Email must be greater than 2 characters', category='error')
        elif len(firstName) < 2 :
            flash('Firstname must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Password don\'t match', category='error')
        elif len(password1) < 8 :
            flash('Password must at least have 8 characters', category='error')
        else:
            #add user to the DB
            flash('Account Created', category='success')
    return render_template("sign_up.html")