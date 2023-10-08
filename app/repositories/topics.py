from .db import connect, pg_connect

from . import sql_queries

from . import mappers, queries


TABLENAME = "topic"


def create(topic_name, description=None):
    new_topic = {"title": topic_name}

    if description:
        new_topic["description"] = description

    with connect() as tx:
        return tx["topic"].insert(new_topic)


def all(order_by=None):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.topics.all_topics)
            return [mappers.topic_mapper(row) for row in cursor.fetchall()]


def active(order_by=None):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.topics.active_topics)
            return [mappers.topic_mapper(row) for row in cursor.fetchall()]


def archived(order_by=None):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.topics.archived_topics)
            return [mappers.topic_mapper(row) for row in cursor.fetchall()]


def update(new_topic_data):
    with connect() as tx:
        tx[TABLENAME].update(new_topic_data, ["id"])


def topic(topic_id):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.topics.topic_by_id, (topic_id,))
            return mappers.topic_mapper(cursor.fetchone())


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


def search_by_title(search_text):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            params = {"search_text": f"%{search_text}%"}
            cursor.execute(sql_queries.topics.search_by_title, params)

            return [mappers.topic_mapper(row) for row in cursor.fetchall()]
