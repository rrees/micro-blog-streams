import flask

from app.auth_password.decorators import login_required


@login_required
def all_tags():
    return flask.render_template("tags/all.html")


tag_routes = [
    ("/tags/all", "tags_all", all_tags, ["GET"]),
]
