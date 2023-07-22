all_topics = """SELECT *
FROM topic
ORDER BY title"""

active_topics = """SELECT *
FROM topic
WHERE active = true
ORDER BY title"""
