import flask

from app.auth_password.decorators import login_required
from app.forms import NewPost
from app.repositories import posts as posts_repository

@login_required
def new_post():
	new_post_form = NewPost(flask.request.form)

	if new_post_form.validate():
		# return flask.redirect(url_for('post', post_id=new_post_id))
		return flask.redirect(flask.url_for('recent'))