-- SQL ALTER statements for database migration

ALTER TABLE topic
	ADD COLUMN created timestamp default current_timestamp;

ALTER TABLE topic
	ADD COLUMN updated timestamp default current_timestamp;


CREATE TRIGGER update_topic_modtime BEFORE UPDATE ON topic FOR EACH ROW EXECUTE PROCEDURE  update_modified_column();
