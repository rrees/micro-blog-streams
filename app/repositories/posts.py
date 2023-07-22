from app import models

from .db import connection, connect, pg_connect

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


def all():
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.posts.all_posts)
            return [post_mapper(r) for r in cursor]


def latest(limit=20):
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.posts.latest_posts, (limit,))
            return [post_mapper(r) for r in cursor]


def create(title, content, tags=None, topic_id=None, url=None):
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
    with connect() as tx:
        return tx[TABLENAME].find_one(id=post_id)


def recent():
    with connect() as tx:
        return queries.read(tx[TABLENAME].find(order_by=["-updated"]), post_mapper)


def by_topic(topic_id, recent=True, limit=None):
    query = (
        "SELECT * from blogpost INNER JOIN topic_posts ON blog_post_id = id WHERE"
        " topic_id = :topic_id ORDER BY updated DESC"
    )

    if limit:
        query = query + " LIMIT :limit"

    with connect() as db:
        return map(post_mapper, db.query(query, topic_id=topic_id, limit=limit))
        # return [post_mapper(table.find_one(id=pid)) for pid in db.query(query, topic_id)]


def update_post(new_post_data):
    with connect() as tx:
        tx[TABLENAME].update(new_post_data, ["id"])


def with_title_matching(search_text):
    with connect() as db:
        return map(post_mapper, db[TABLENAME].find(title={"ilike": f"%{search_text}%"}))


def with_tag(tag):
    query = "SELECT * FROM blogpost WHERE :tag = ANY(tags)"
    with connect() as db:
        return map(post_mapper, db.query(query, tag=tag))
