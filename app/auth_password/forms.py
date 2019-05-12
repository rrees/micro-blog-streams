from wtforms import Form, validators
from wtforms import fields

class Login(Form):
    email = fields.StringField('Username', [validators.required()])
    password = fields.PasswordField('Password', [validators.required()])