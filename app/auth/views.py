from flask import render_template
from app.form import LoginForm
from . import auth

# ROUTES CREATION
@auth.route('/login')
def login():
    print('in login')
    context = {
        'login_form' : LoginForm()
    }

    return render_template('login.html', **context)
    #return 'hi'