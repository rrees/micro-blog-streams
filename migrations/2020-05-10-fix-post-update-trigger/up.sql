-- SQL ALTER statements for database migration

DROP TRIGGER IF EXISTS update_blogpost_modtime ON blogpost;

CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated = now();
    RETURN NEW; 
END;
$$ language 'plpgsql';

CREATE TRIGGER update_blogpost_modtime
BEFORE UPDATE ON blogpost
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
