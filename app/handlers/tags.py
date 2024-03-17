import flask

from app.auth_password.decorators import login_required

from app.repositories import tags


@login_required
def all_tags():
    all_tags = tags.all_tags()
    return flask.render_template("tags/all.html", tags=all_tags)


tag_routes = [
    ("/tags/all", "all_tags", all_tags, ["GET"]),
]
