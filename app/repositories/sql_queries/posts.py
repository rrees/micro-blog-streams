all_posts = """SELECT *
FROM blogpost"""

latest_posts = """SELECT *
FROM blogpost
ORDER BY updated DESC
LIMIT %s"""
