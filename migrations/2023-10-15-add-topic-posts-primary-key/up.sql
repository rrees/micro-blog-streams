-- SQL ALTER statements for database migration

ALTER TABLE topic_posts
ALTER COLUMN blog_post_id SET DATA TYPE integer,
ALTER COLUMN topic_id SET DATA TYPE integer;

ALTER TABLE topic_posts ADD PRIMARY KEY (blog_post_id, topic_id);