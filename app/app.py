import os
import logging

import flask

from flask_sslify import SSLify

from . import handlers
from . import redis_utils
from .auth_password.routes import auth_routes

ENV = os.environ.get("ENV", "PROD")

redis_url = os.environ.get("REDIS_URL", None)

redis = redis_utils.setup_redis(redis_url) if redis_url else None

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

if not ENV == "DEV":
    sslify = SSLify(app)

logger = app.logger

routes = [
	('/', 'index', handlers.pages.front_page, ['GET']),
	('/home', 'home', handlers.pages.home, ['GET']),
	('/recent', 'recent', handlers.pages.recent_posts, ['GET']),
	('/topics', 'topics', handlers.pages.topics, ['GET']),
	('/topic/<topic_id>', 'topic', handlers.pages.topic, ['GET']),
	('/topics/new', 'new_topic', handlers.pages.new_topic, ['GET']),
	('/forms/topic/new', 'new_topic_form', handlers.forms.new_topic, ['POST']),
	('/posts/new', 'new_post', handlers.pages.new_post, ['GET']),
	('/forms/post/new', 'new_post_form', handlers.forms.new_post, ['POST']),
	('/post/<post_id>', 'post', handlers.pages.post, ['GET']),
]

routes = routes + auth_routes

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500