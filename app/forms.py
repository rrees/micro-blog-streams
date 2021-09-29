from wtforms import Form, validators
from wtforms import fields


class Post(Form):
    title = fields.StringField('Title', [validators.InputRequired()])
    content = fields.TextAreaField('Content', [validators.InputRequired()])
    topic_id = fields.IntegerField()
    url = fields.StringField('URL', [validators.Optional()])
    tags = fields.StringField('Tags', [validators.Optional()])


class Topic(Form):
    title = fields.StringField('Title', [validators.InputRequired()])
    description = fields.StringField('Description', [])


class TopicId(Form):
    topic_id = fields.IntegerField('Id', [validators.InputRequired()])
