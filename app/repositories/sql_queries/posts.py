all_posts = """SELECT *
FROM blogpost"""

latest_posts = """SELECT *
FROM blogpost
ORDER BY updated DESC
LIMIT %s"""

by_topic = """SELECT *
FROM blogpost
INNER JOIN topic_posts
ON blog_post_id = id
WHERE topic_id = %s
ORDER BY updated DESC
LIMIT %s"""

with_tag = """SELECT *
FROM blogpost
WHERE %s = ANY(tags)"""
