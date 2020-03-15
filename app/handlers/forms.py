import flask

from app.auth_password.decorators import login_required
from app.repositories import posts as posts_repository

@login_required
def new_post():

	# return flask.redirect(url_for('post', post_id=new_post_id))
	return flask.redirect(flask.url_for('recent'))