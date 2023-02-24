from application import app
from functools import wraps
from flask import render_template, url_for, request, redirect, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


def loginHandler():
    email = request.form['email']
    password = request.form['password']
    psw = "pbkdf2:sha256:260000$SIZTTnBvrZ4c8Ksl$a4155edb2a53056a75a2ec54de5e8604c52c14bbb21a9f0e6eed89f55443c80d"
    if check_password_hash(psw, password):
        session['loggedin'] = True
        return {"status": True}
    return {"status": False}


def usersLoginRequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # print('loggedin' not in session)
        # print('user' not in session)
        # print('loggedin' not in session and 'user' not in session)
        if 'loggedin' in session:
            return f(*args, **kwargs)
        return redirect(url_for('login'))
    return decorated_function


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('admin', None)
    session.pop('id', None)
    session.pop('user', None)
    return redirect(url_for('login'))
