import flask

from app.auth_password.decorators import login_required
from app import repositories

def front_page():
	return flask.render_template('index.html')

@login_required
def home():
	recent_posts = repositories.posts.recent()
	topics = repositories.topics.all()
	return flask.render_template('home.html',
		recent_posts=recent_posts,
		topics=topics)

@login_required
def recent_posts():
	return flask.render_template('recent.html',
		recent_posts = repositories.posts.latest()
		)

@login_required
def topics():
	return flask.render_template('topics.html',
		topics = repositories.topics.all()
		)


@login_required
def topic(topic_id):
	return flask.render_template('topic.html',
		topic = repositories.topics.topic(topic_id),
		recent_posts=repositories.posts.by_topic(topic_id)
		)


@login_required
def post(post_id):
	return flask.render_template('post.html',
		post = repositories.posts.post(post_id)
		)

@login_required
def new_post():
	return flask.render_template('posts/new.html')


@login_required
def new_topic():
	return flask.render_template('topics/new.html')

@login_required
def edit_post(post_id):
	return flask.render_template(
		'posts/edit.html',
		post = repositories.posts.post(post_id)
	)