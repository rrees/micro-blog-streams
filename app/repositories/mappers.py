from app import models


def topic_mapper(topic):
	if not topic:
		return None
	return models.Topic(
		id = topic['id'],
		title = topic['title'],
		tags = topic['tags'],
		description = topic['description'] if 'description' in topic else '',
		updated = topic['updated'] if 'updated' in topic else None,
		active = topic['active'])