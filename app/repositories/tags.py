from .posts import query_posts

from . import sql_queries


def find_posts_by_tag(tag_name):
    return query_posts(sql_queries.posts.search_by_tag, {"tag_name": tag_name})
