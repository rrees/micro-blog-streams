all_posts = """SELECT *
FROM blogpost"""

latest_posts = """SELECT *
FROM blogpost
ORDER BY updated DESC
LIMIT %s"""

by_id = """SELECT *
FROM blogpost
WHERE id = %s"""

by_topic = """SELECT *
FROM blogpost
INNER JOIN topic_posts
ON blog_post_id = id
WHERE topic_id = %(topic_id)s
ORDER BY updated DESC
LIMIT %(limit)s"""

with_tag = """SELECT *
FROM blogpost
WHERE %s = ANY(tags)"""

remove_topic = """DELETE FROM topic_posts
WHERE topic_id = %(topic_id)s
AND blog_post_id = %(post_id)s"""

delete = """DELETE
FROM blogpost
WHERE id = %(post_id)s"""

remove_all_topics = """DELETE
FROM topic_posts
WHERE blog_post_id = %(post_id)s"""

search_by_title = """SELECT *
FROM blogpost
WHERE title ilike %(search_text)s"""
