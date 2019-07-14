import os

import dataset

from app import models

db = dataset.connect(os.environ["DATABASE_URL"])
table = db['topic']

def topic_mapper(topic):
	if not topic:
		return None
	return models.Topic(
		id = topic['id'],
		title = topic['title'],
		tags = topic['tags'])

def create(topic_name):
	table.insert({"title": topic_name})
	return topic_name

def all():
	return [topic_mapper(r) for r in table]