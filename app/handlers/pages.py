import itertools

import flask

from app.auth_password.decorators import login_required
from app import repositories, search_forms, models


def front_page():
    return flask.render_template("index.html")


@login_required
def home():
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
        all_topics=repositories.topics.all(order_by="name"),
    )


@login_required
def post_raw(post_id):
    return flask.render_template(
        "posts/raw.html",
        post=repositories.posts.post(post_id),
        topics=repositories.topics.for_post(post_id),
    )


@login_required
def search():
    return flask.render_template("search.html")


@login_required
def search_posts_by_title():
    search_form = search_forms.SearchForm(flask.request.form)
    return_link = None

    if search_form.validate():
        posts, posts_test = itertools.tee(
            repositories.posts.with_title_matching(search_form.search_term.data)
        )

        try:
            next(posts_test)
        except StopIteration:
            return_link = models.ReturnLink(
                path=flask.url_for("search"), text="Search again"
            )

        return flask.render_template(
            "posts-list.html",
            page_title="Search results",
            posts=list(posts),
            return_link=return_link,
        )

    flask.abort(400, "Form information incorrect")


@login_required
def posts_by_tag(tag):
    posts = repositories.posts.with_tag(tag)
    return flask.render_template(
        "posts-list.html", page_title=f"Search results for tag {tag}", posts=list(posts)
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


@login_required
def search_topics_by_title():
    search_form = search_forms.SearchForm(flask.request.form)
    return_link = None

    if search_form.validate():
        topics = repositories.topics.search_by_title(search_form.search_term.data)

        if not topics:
            return_link = models.ReturnLink(
                path=flask.url_for("search"), text="Search again"
            )

        return flask.render_template(
            "topics.html",
            page_title="Search results",
            topics=topics,
            return_link=return_link,
        )

    flask.abort(400, "Form information incorrect")
