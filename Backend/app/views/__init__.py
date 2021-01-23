
from flask import Blueprint
from flask_restx import Api, Resource
from flask_cors import CORS

api_resources = Blueprint("api_resources", __name__)

CORS(api_resources)

authorizations = {
    'apikey':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}

api_call = Api(title="MINI UNSPLASH API DOC", doc="/doc", description="This was written by Ewanfo Lucky Peter", authorizations=authorizations, security='apikey')

api_call.init_app(api_resources)


#########################################
#USERS API NAMESPACE#####
#########################################

users_api_call = api_call.namespace("Users Endpoints", path="/users")

from app.views import users_api_resources

#########################################
#IMAGES API NAMESPACE#####
#########################################

images_api_call = api_call.namespace("Images Endpoints", path="/images")

from app.views import images_api_resources