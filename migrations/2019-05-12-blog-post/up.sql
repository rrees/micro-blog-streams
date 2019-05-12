-- SQL ALTER statements for database migration
CREATE TABLE blogpost(
	id serial,
	title text,
	content text,
	tags text[],
	created timestamp default current_timestamp,
	updated timestamp default current_timestamp
);

CREATE OR REPLACE FUNCTION update_modified_column() 
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified = now();
    RETURN NEW; 
END;
$$ language 'plpgsql';

CREATE TRIGGER update_blogpost_modtime BEFORE UPDATE ON blogpost FOR EACH ROW EXECUTE PROCEDURE  update_modified_column();
