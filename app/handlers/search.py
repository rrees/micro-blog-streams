import itertools

import flask

from app.auth_password.decorators import login_required
from app import repositories, search_forms, models


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
def search_posts_by_content():
    search_form = search_forms.SearchForm(flask.request.form)
    return_link = None

    if search_form.validate():
        posts = repositories.posts.with_content_matching(search_form.search_term.data)

        return flask.render_template(
            "posts-list.html",
            page_title="Search results",
            posts=posts,
            return_link=return_link,
            preview_content=True,
        )

    flask.abort(400, "Form information incorrect")


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


search_routes = [
    ("/search", "search", search, ["GET"]),
    (
        "/search/posts/title",
        "search_posts_by_title",
        search_posts_by_title,
        ["POST"],
    ),
    (
        "/search/posts/content",
        "search_posts_by_content",
        search_posts_by_content,
        ["POST"],
    ),
    (
        "/search/topics/title",
        "search_topics_by_title",
        search_topics_by_title,
        ["POST"],
    ),
]
