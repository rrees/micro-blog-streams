import flask

from app.auth_password.decorators import login_required

@login_required
def menu_topics():
    return flask.render_template("menus/topics.html")


menu_routes = [
    ('/menus/topics', 'menu_topics', menu_topics, ['GET']),
]