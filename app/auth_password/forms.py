from wtforms import Form, validators
from wtforms import fields


class Login(Form):
    email = fields.StringField("Username", [validators.InputRequired()])
    password = fields.PasswordField("Password", [validators.InputRequired()])
