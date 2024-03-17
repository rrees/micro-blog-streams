from .posts import query_posts

from . import sql_queries

from .db import pg_connect


def find_posts_by_tag(tag_name):
    return query_posts(sql_queries.posts.search_by_tag, {"tag_name": tag_name})


def all_tags():
    with pg_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_queries.tags.all_tags)
            return [tag["tag"] for tag in cursor if tag["tag"]]
