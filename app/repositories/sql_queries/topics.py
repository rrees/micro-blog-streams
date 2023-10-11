all_topics = """SELECT *
FROM topic
ORDER BY title"""

active_topics = """SELECT *
FROM topic
WHERE active = true
ORDER BY title"""

archived_topics = """SELECT *
FROM topic
WHERE active = true
ORDER BY title"""

topic_by_id = """SELECT *
FROM topic
WHERE id = %s"""

search_by_title = """SELECT *
FROM topic
WHERE title ilike %(search_text)s"""

for_post = """SELECT topic_id
FROM topic_posts
WHERE blog_post_id = %(post_id)s"""

create = """INSERT INTO topic ({})
VALUES ({})
RETURNING id"""

delete = """DELETE FROM topic
WHERE id= %(topic_id)s"""
