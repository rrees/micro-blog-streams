from app import models

from .db import connection, connect

TABLENAME = "blogpost"

db = connection
table = db[TABLENAME]

def post_mapper(post):
	if not post:
		return None
	return models.BlogPost(
		id = post['id'],
		title = post['title'],
		content = post['content'],
		tags = post['tags'])

def all():
	return [post_mapper(r) for r in table]

def latest():
	return [
		post_mapper(r)
		for r
		in table.find(_limit=20, order_by='updated')
	]

def create(title, content, tags=None):
	with connect() as tx:
		post_data = {"title": title, "content": content}

		if tags:
			post_data['tags'] = tags
		return tx[TABLENAME].insert(post_data)

def read(post_id):
	db = connect()
	return db[TABLENAME].find_one(id=post_id)