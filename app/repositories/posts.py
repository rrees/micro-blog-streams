from app import models

from .db import connection, connect

from . import mappers
from . import queries

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
		tags = post['tags'],
		updated = post['updated'])

def all():
	return [post_mapper(r) for r in table]

def latest():
	return [
		post_mapper(r)
		for r
		in table.find(_limit=20, order_by='-updated')
	]

def create(title, content, tags=None, topic_id=None):
	with connect() as tx:
		post_data = {"title": title, "content": content}

		if tags:
			post_data['tags'] = tags

		post_id = tx[TABLENAME].insert(post_data)

		if topic_id:
			topic_posts = tx['topic_posts']
			topic_posts.insert({
				'blog_post_id': post_id,
				'topic_id': topic_id,
				})

		return post_id

def post(post_id):
	db = connect()
	return db[TABLENAME].find_one(id=post_id)

def recent():
	return queries.read(table.find(order_by=['-updated']), post_mapper)