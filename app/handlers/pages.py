import flask

def front_page():
	return flask.render_template('index.html')