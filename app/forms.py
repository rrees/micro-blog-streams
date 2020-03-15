from wtforms import Form, validators
from wtforms import fields

class NewPost(Form):
	title = fields.StringField('Title',
		[validators.InputRequired()])
	content = fields.TextAreaField('Content',
		[validators.InputRequired()])