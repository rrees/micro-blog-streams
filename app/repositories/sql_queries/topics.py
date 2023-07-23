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
