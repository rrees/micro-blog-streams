import os
import logging

import flask

from . import handlers
from . import redis_utils
from .auth_password.routes import auth_routes
from .filters import custom_filters

ENV = os.environ.get("ENV", "PROD")

redis_url = os.environ.get("REDIS_URL", None)

redis = redis_utils.setup_redis(redis_url) if redis_url else None

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Strict",
)

logger = app.logger

routes = [
    ("/", "index", handlers.pages.front_page, ["GET"]),
    ("/home", "home", handlers.pages.home, ["GET"]),
    ("/everything", "everything", handlers.pages.everything, ["GET"]),
    ("/recent", "recent", handlers.pages.recent_posts, ["GET"]),
    ("/topics", "topics", handlers.pages.topics, ["GET"]),
    ("/topics/all", "all_topics", handlers.pages.all_topics, ["GET"]),
    ("/topics/archived", "archived_topics", handlers.pages.archived_topics, ["GET"]),
    ("/topic/<topic_id>", "topic", handlers.pages.topic, ["GET"]),
    ("/topic/<topic_id>/edit", "edit_topic", handlers.pages.edit_topic, ["GET"]),
    (
        "/forms/topic/<topic_id>/edit",
        "edit_topic_form",
        handlers.forms.edit_topic,
        ["POST"],
    ),
    ("/topics/new", "new_topic", handlers.pages.new_topic, ["GET"]),
    ("/forms/topic/new", "new_topic_form", handlers.forms.new_topic, ["POST"]),
    (
        "/forms/topic/delete/<topic_id>",
        "delete_topic_form",
        handlers.forms.delete_topic,
        ["POST"],
    ),
    ("/topic/<topic_id>/delete", "delete_topic", handlers.pages.delete_topic, ["GET"]),
    (
        "/topic/<topic_id>/archive",
        "archive_topic",
        handlers.pages.archive_topic,
        ["GET"],
    ),
    (
        "/forms/topic/<topic_id>/archive",
        "archive_topic_form",
        handlers.forms.archive_topic,
        ["POST"],
    ),
    (
        "/forms/topic/<topic_id>/unarchive",
        "unarchive_topic_form",
        handlers.forms.unarchive_topic,
        ["POST"],
    ),
    (
        "/topic/<topic_id>/posts/all",
        "all_posts_for_topic",
        handlers.pages.all_posts_for_topic,
        ["GET"],
    ),
    ("/posts/new", "new_post", handlers.pages.new_post, ["GET"]),
    ("/forms/post/new", "new_post_form", handlers.forms.new_post, ["POST"]),
    ("/post/<post_id>", "post", handlers.pages.post, ["GET"]),
    ("/post/<post_id>/raw", "post_raw", handlers.pages.post_raw, ["GET"]),
    ("/post/<post_id>/edit", "edit_post", handlers.pages.edit_post, ["GET"]),
    (
        "/forms/post/<post_id>/edit",
        "edit_post_form",
        handlers.forms.edit_post,
        ["POST"],
    ),
    (
        "/post/<post_id>/topics/edit",
        "edit_post_topics",
        handlers.pages.edit_post_topics,
        ["GET"],
    ),
    (
        "/post/<post_id>/topics/add",
        "add_post_to_topic",
        handlers.forms.add_post_to_topic,
        ["POST"],
    ),
    (
        "/post/<post_id>/topics/remove",
        "remove_topic_from_post",
        handlers.forms.remove_topic_from_post,
        ["POST"],
    ),
    ("/posts/all", "all_posts", handlers.pages.all_posts, ["GET"]),
    ("/posts/all/tag/<tag>", "posts_by_tag", handlers.pages.posts_by_tag, ["GET"]),
    ("/search", "search", handlers.pages.search, ["GET"]),
    (
        "/search/posts/title",
        "search_posts_by_title",
        handlers.pages.search_posts_by_title,
        ["POST"],
    ),
    (
        "/search/topics/title",
        "search_topics_by_title",
        handlers.pages.search_topics_by_title,
        ["POST"],
    ),
    (
        "/manifest.json",
        "manifest",
        handlers.pages.manifest,
        ["GET"],
    ),
]

routes = routes + auth_routes + handlers.navigation.navigation_routes

for path, endpoint, handler, methods in routes:
    app.add_url_rule(path, endpoint, handler, methods=methods)

for name, custom_filter in custom_filters:
    app.jinja_env.filters[name] = custom_filter


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception("An error occurred during a request.")
    return "An internal error occurred.", 500
