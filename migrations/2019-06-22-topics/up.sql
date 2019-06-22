ALTER TABLE blogpost
ADD PRIMARY KEY (id);

CREATE TABLE topic (
	id serial CONSTRAINT topic_id PRIMARY KEY,
	title text,
	tags text[]
);

CREATE TABLE topic_posts (
	blog_post_id serial references blogpost(id),
	topic_id serial references topic(id)
);