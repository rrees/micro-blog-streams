import datetime

import mistune

markdown_renderer = mistune.Markdown()

def markdown(markdown):
	return markdown_renderer(markdown)

def iso_date(a_date):
	return a_date.isoformat(timespec='seconds')

custom_filters = (
	('markdown', markdown),
	('iso_date', iso_date),
)