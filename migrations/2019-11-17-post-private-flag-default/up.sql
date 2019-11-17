-- SQL ALTER statements for database migration

ALTER TABLE blogpost
DROP COLUMN private;

ALTER TABLE blogpost
ADD COLUMN private BOOLEAN NOT NULL DEFAULT false;	