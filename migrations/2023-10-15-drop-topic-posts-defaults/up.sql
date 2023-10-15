-- SQL ALTER statements for database migration

ALTER TABLE topic_posts
ALTER COLUMN blog_post_id DROP DEFAULT,
ALTER COLUMN topic_id DROP DEFAULT;