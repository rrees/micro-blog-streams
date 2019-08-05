import flask

from app.auth_password.decorators import login_required
from app import repositories

def front_page():
	return flask.render_template('index.html')

@login_required
def home():
	return flask.render_template('home.html')

@login_required
def recent_posts():
	return flask.render_template('recent.html',
		recent_posts = repositories.posts.latest()
		)