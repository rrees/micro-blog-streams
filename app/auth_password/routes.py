from . import handlers

auth_routes = [
    ('/auth/forms/login', 'login_form', handlers.login_form, ['POST']),
]