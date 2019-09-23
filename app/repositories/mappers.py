from app import models


def topic_mapper(topic):
	if not topic:
		return None
	return models.Topic(
		id = topic['id'],
		title = topic['title'],
		tags = topic['tags'])