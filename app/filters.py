import mistune

markdown_renderer = mistune.Markdown()

def markdown(markdown):
	return markdown_renderer(markdown)

custom_filters = (
	('markdown', markdown),
)