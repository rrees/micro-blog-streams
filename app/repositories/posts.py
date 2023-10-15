from app import models

from .db import connection, connect, format_placeholders, pg_connect

from . import mappers
from . import queries
from . import sql_queries

TABLENAME = "blogpost"

db = connection
table = db[TABLENAME]
topic_posts = db["topic_posts"]


def post_mapper(post):
    if not post:
        return None
    return models.BlogPost(
        id=post["id"],
        title=post["title"],
        content=post["content"],
        tags=post["tags"],
        updated=post["updated"],
    )


def query_posts(query, params=None):
    if not params:
        params = {}

    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return [post_mapper(r) for r in cursor]


def all():
    return query_posts(sql_queries.posts.all_posts)


def latest(limit=20):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.posts.latest_posts, (limit,))
            return [post_mapper(r) for r in cursor]


def create(title, content, tags=None, topic_id=None, url=None):
    post_data = {"title": title, "content": content}

    if tags:
        post_data["tags"] = tags

    if url:
        post_data["url"] = url

    with pg_connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                query = format_placeholders(sql_queries.posts.create, post_data.keys())
                cursor.execute(query, post_data)
                new_post_id = cursor.fetchone()["id"]
                cursor.execute(
                    sql_queries.topic_posts.add,
                    {"post_id": new_post_id, "topic_id": topic_id},
                )
                return new_post_id
    with connect() as tx:
        post_data = {"title": title, "content": content}

        if tags:
            post_data["tags"] = tags

        if url:
            post_data["url"] = url

        post_id = tx[TABLENAME].insert(post_data)

        if topic_id:
            topic_posts = tx["topic_posts"]
            topic_posts.insert({"blog_post_id": post_id, "topic_id": topic_id})

        return post_id


def post(post_id):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.posts.by_id, (post_id,))
            return post_mapper(cursor.fetchone())


def recent():
    return query_posts(sql_queries.posts.recent)


def by_topic(topic_id, recent=True, limit=None):
    query = sql_queries.posts.by_topic
    params = {"topic_id": topic_id, "limit": limit}

    return query_posts(query, params)


def update_post(new_post_data):
    with connect() as tx:
        tx[TABLENAME].update(new_post_data, ["id"])


def with_title_matching(search_text):
    params = {"search_text": f"%{search_text}%"}
    return query_posts(sql_queries.posts.search_by_title, params)


def with_tag(tag):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.posts.with_tag, (tag,))
            return [post_mapper(row) for row in cursor]


def remove_topic(post_id, topic_id):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                parameters = {"post_id": post_id, "topic_id": topic_id}
                cursor.execute(sql_queries.posts.remove_topic, parameters)
                return post_id


def delete(post_id):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                parameters = {"post_id": post_id}
                cursor.execute(sql_queries.posts.remove_all_topics, parameters)
                cursor.execute(sql_queries.posts.delete, parameters)
                return post_id
