import flask

from app.auth_password.decorators import login_required

@login_required
def navigation_topics():
    return flask.render_template("navigation/topics.html")


navigation_routes = [
    ('/navigation/topics', 'navigation_topics', navigation_topics, ['GET']),
]