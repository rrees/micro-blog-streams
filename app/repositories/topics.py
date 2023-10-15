from .db import connect, execute_statement, format_placeholders, pg_connect

from . import sql_queries

from . import mappers, queries


TABLENAME = "topic"


def create(topic_name, description=None):
    new_topic = {"title": topic_name}

    if description:
        new_topic["description"] = description

    with pg_connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                query = format_placeholders(sql_queries.topics.create, new_topic.keys())
                cursor.execute(query, new_topic)
                return cursor.fetchone()["id"]


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
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                statement = format_placeholders(
                    sql_queries.topics.update,
                    [k for k in new_topic_data.keys() if k != "topic_id"],
                )
                cursor.execute(statement, new_topic_data)


def topic(topic_id):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.topics.topic_by_id, (topic_id,))
            return mappers.topic_mapper(cursor.fetchone())


def for_post(post_id):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.topics.for_post, {"post_id": post_id})
            return [topic(result["topic_id"]) for result in cursor.fetchall()]


def delete(topic_id):
    params = {"topic_id": topic_id}

    with pg_connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                cursor.execute(sql_queries.topic_posts.delete_by_topic, params)
                cursor.execute(sql_queries.topics.delete, params)
                return topic_id


def add_post_to_topic(post_id, topic_id):
    params = {"post_id": post_id, "topic_id": topic_id}
    execute_statement(sql_queries.topic_posts.add, params)
    return post_id


def remove_post_from_topic(post_id, topic_id):
    params = {"post_id": post_id, "topic_id": topic_id}
    execute_statement(sql_queries.topic_posts.delete, params)
    return topic_id


def active_flag(topic_id, active_flag):
    params = {"topic_id": topic_id, "active_flag": active_flag}
    execute_statement(sql_queries.topics.active_flag, params)
    return topic_id


def search_by_title(search_text):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            params = {"search_text": f"%{search_text}%"}
            cursor.execute(sql_queries.topics.search_by_title, params)

            return [mappers.topic_mapper(row) for row in cursor.fetchall()]
