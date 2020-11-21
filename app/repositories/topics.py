
from .db import connection

from . import mappers, queries

db = connection
table = db['topic']

def create(topic_name, description=None):
	new_topic = {"title": topic_name}

	if description:
		new_topic['description'] = description

	return table.insert(new_topic)

def all(order_by=None):
	return queries.read(table.all(order_by='title'), mappers.topic_mapper)

def update(topic):
	with db as tx:
		tx['topic'].update(topic, ['id'])
		return tx['topic'].find_one(id=topic['id'])

def topic(topic_id):
	return mappers.topic_mapper(table.find_one(id=topic_id))
