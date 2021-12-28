from wtforms import Form, validators
from wtforms import fields


class SearchForm(Form):
    search_term = fields.StringField("Term", [validators.InputRequired()])
