import flask

from app.auth_password.decorators import login_required
from app import repositories, search_forms, models


def front_page():
    return flask.render_template("index.html")


@login_required
def home():
    return flask.render_template("navigation/menu.html")


@login_required
def everything():
    posts = repositories.posts.latest(limit=50)
    topics = repositories.topics.active()
    return flask.render_template("home.html", posts=posts, topics=topics)


@login_required
def recent_posts():
    return flask.render_template(
        "posts-list.html", page_title="Recent posts", posts=repositories.posts.latest()
    )


@login_required
def all_posts():
    return flask.render_template(
        "posts-list.html", page_title="All posts", posts=repositories.posts.all()
    )


@login_required
def topics():
    return flask.render_template(
        "topics.html",
        topics=repositories.topics.active(),
    )


@login_required
def all_topics():
    return flask.render_template(
        "topics.html",
        page_title="All Topics",
        topics=repositories.topics.all(),
    )


@login_required
def archived_topics():
    return flask.render_template(
        "topics.html",
        page_title="Archived Topics",
        topics=repositories.topics.archived(),
    )


@login_required
def topic(topic_id):
    return flask.render_template(
        "topic.html",
        topic=repositories.topics.topic(topic_id),
        recent_posts=repositories.posts.by_topic(topic_id, limit=20),
    )


@login_required
def post(post_id):
    return flask.render_template(
        "post.html",
        post=repositories.posts.post(post_id),
        topics=repositories.topics.for_post(post_id),
    )


@login_required
def new_post():
    return flask.render_template("posts/new.html", title_required=True)


@login_required
def new_topic():
    return flask.render_template("topics/new.html")


@login_required
def edit_topic(topic_id):
    return flask.render_template(
        "topics/edit.html", topic=repositories.topics.topic(topic_id)
    )


@login_required
def archive_topic(topic_id):
    topic = repositories.topics.topic(topic_id)
    return flask.render_template(
        "topics/archive.html",
        topic=topic,
    )


@login_required
def delete_topic(topic_id):
    return flask.render_template(
        "topics/delete.html", topic=repositories.topics.topic(topic_id)
    )


@login_required
def edit_post(post_id):
    return flask.render_template(
        "posts/edit.html", post=repositories.posts.post(post_id)
    )


@login_required
def edit_post_topics(post_id):
    return flask.render_template(
        "posts/edit-topics.html",
        post=repositories.posts.post(post_id),
        post_topics=repositories.topics.for_post(post_id),
        all_topics=repositories.topics.all(),
    )


@login_required
def post_raw(post_id):
    return flask.render_template(
        "posts/raw.html",
        post=repositories.posts.post(post_id),
        topics=repositories.topics.for_post(post_id),
    )


@login_required
def posts_by_tag(tag):
    posts = repositories.posts.with_tag(tag)
    return flask.render_template(
        "posts-list.html",
        page_title=f'Search results for tag "{tag}"',
        posts=list(posts),
    )


@login_required
def all_posts_for_topic(topic_id):
    topic = repositories.topics.topic(topic_id)
    posts = repositories.posts.by_topic(topic_id)

    return flask.render_template(
        "topics/all-posts.html",
        topic=topic,
        posts=posts,
    )


def manifest():
    manifest = {
        "name": "Micro Blog Streams",
        "display": "browser",
        "start_url": flask.url_for("index"),
        "icons": [
            {
                "src": flask.url_for(
                    "static", filename="images/micro-blog-stream-logo.svg"
                ),
                "sizes": "any",
                "type": "image/svg+xml",
                "purpose": "maskable",
            }
        ],
    }
    return flask.jsonify(manifest)
