import flask

from app.auth_password.decorators import login_required

def front_page():
	return flask.render_template('index.html')

@login_required
def home():
	return flask.render_template('home.html')