from functools import wraps
from flask import session, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            #return redirect(url_for('index', next=request.url))
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function