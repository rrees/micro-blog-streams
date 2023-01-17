from .db import connect

from . import mappers, queries

TABLENAME = "topic"


def create(topic_name, description=None):
    new_topic = {"title": topic_name}

    if description:
        new_topic["description"] = description

    with connect() as tx:
        return tx["topic"].insert(new_topic)


def all(order_by=None):
    with connect() as tx:
        return queries.read(tx[TABLENAME].all(order_by="title"), mappers.topic_mapper)

def active(order_by=None):
    with connect() as tx:
        return queries.read(tx[TABLENAME].all(active=True, order_by="title"), mappers.topic_mapper)


def update(new_topic_data):
    with connect() as tx:
        table.update(new_topic_data, ["id"])


def topic(topic_id):
    with connect() as db:
        return mappers.topic_mapper(db[TABLENAME].find_one(id=topic_id))


def for_post(post_id):
    with connect() as tx:
        topic_links = tx["topic_posts"].find(blog_post_id=post_id)
        return [topic(topic_link["topic_id"]) for topic_link in topic_links]


def delete(topic_id):
    with connect() as tx:
        tx["topic_posts"].delete(topic_id=topic_id)
        tx["topic"].delete(id=topic_id)

        return topic_id


def add_post_to_topic(post_id, topic_id):
    with connect() as tx:
        row = {"blog_post_id": post_id, "topic_id": topic_id}
        tx["topic_posts"].insert_ignore(row, ["blog_post_id", "topic_id"])
        return post_id


def remove_post_from_topic(post_id, topic_id):
    with connect() as tx:
        row_filter = {"blog_post_id": post_id, "topic_id": topic_id}
        tx["topic_posts"].delete(**row_filter)
        return post_id

def active_flag(topic_id, active_flag):
    with connect() as tx:
        tx["topic"].update({"id": topic_id, "active": active_flag}, ["id"])

        return topic_id
