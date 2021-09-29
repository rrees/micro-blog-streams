from .db import connection, connect

from . import mappers, queries

db = connection
table = db['topic']


def create(topic_name, description=None):
    new_topic = {"title": topic_name}

    if description:
        new_topic['description'] = description

    with connect() as tx:
        return tx['topic'].insert(new_topic)


def all(order_by=None):
    return queries.read(table.all(order_by='title'), mappers.topic_mapper)


def update(new_topic_data):
    with connect() as tx:
        table.update(new_topic_data, ['id'])


def topic(topic_id):
    return mappers.topic_mapper(table.find_one(id=topic_id))


def for_post(post_id):
    with db as tx:
        topic_links = tx['topic_posts'].find(blog_post_id=post_id)
        return [topic(topic_link['topic_id']) for topic_link in topic_links]


def delete(topic_id):
    with db as tx:
        tx['topic_posts'].delete(topic_id=topic_id)
        tx['topic'].delete(id=topic_id)

        return topic_id


def add_post_to_topic(post_id, topic_id):
    with db as tx:
        row = {"blog_post_id": post_id, "topic_id": topic_id}
        tx['topic_posts'].insert_ignore(row, ["blog_post_id", "topic_id"])
        return post_id
