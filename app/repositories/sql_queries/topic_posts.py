delete_by_topic = """DELETE FROM topic_posts
WHERE topic_id = %(topic_id)s"""

delete = """DELETE FROM topic_posts
WHERE blog_post_id = %(post_id)s
AND topic_id = %(topic_id)s"""

add = """INSERT INTO topic_posts (
	blog_post_id,
	topic_id
)
VALUES (
%(post_id)s,
%(topic_id)s
)
ON CONFLICT (
	blog_post_id,
	topic_id
)
DO NOTHING
RETURNING *
"""
