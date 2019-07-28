from app import models

from .db import connection

db = connection
table = db['topic']

def topic_mapper(topic):
	if not topic:
		return None
	return models.Topic(
		id = topic['id'],
		title = topic['title'],
		tags = topic['tags'])

def create(topic_name):
	return table.insert({"title": topic_name})

def all():
	return [topic_mapper(r) for r in table]

def update(topic):
	with db as tx:
		tx['topic'].update(topic, ['id'])
		return tx['topic'].find_one(id=topic['id'])

