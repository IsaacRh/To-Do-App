from flask import render_template
from app.form import LoginForm
from . import auth
from app.firestore_service import get_users

# ROUTES CREATION
@auth.route('/login')
def login():
    print('in login')
    users = get_users()
    for user in users:
        print(user)
    context = {
        'login_form' : LoginForm()
    }

    return render_template('login.html', **context)
    #return 'hi'