
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

