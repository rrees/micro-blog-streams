
from .db import connection

from . import mappers, queries

db = connection
table = db['topic']

def create(topic_name):
	return table.insert({"title": topic_name})

def all():
	return queries.read(table, mappers.topic_mapper)

def update(topic):
	with db as tx:
		tx['topic'].update(topic, ['id'])
		return tx['topic'].find_one(id=topic['id'])

def topic(topic_id):
	return mappers.topic_mapper(table.find_one(id=topic_id))

