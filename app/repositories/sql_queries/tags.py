all_tags = """SELECT DISTINCT(UNNEST(tags)) AS tag
FROM blogpost
ORDER BY tag"""
