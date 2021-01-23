from app.views import users_api_call
from flask_restx import fields

user_login_model = users_api_call.model("User Login", {
    "username":fields.String("username"),
    "password":fields.String("password")
})

user_registration_model = users_api_call.model("User Registration", {
    "username":fields.String("username"),
    "password":fields.String("password")
})