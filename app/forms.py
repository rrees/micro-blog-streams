from wtforms import Form, validators
from wtforms import fields

class Post(Form):
	title = fields.StringField('Title',
		[validators.InputRequired()])
	content = fields.TextAreaField('Content',
		[validators.InputRequired()])
	topic_id = fields.IntegerField()
	url = fields.StringField('URL', [validators.Optional()])
	tags = fields.StringField('Tags', [validators.Optional()])


class NewTopic(Form):
	title = fields.StringField('Title',
		[validators.InputRequired()])
	description = fields.StringField('Description', [])