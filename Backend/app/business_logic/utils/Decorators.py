import jwt, time
from functools import wraps
from config import config
from flask import request, make_response
from app.business_logic.utils.DBFunctionsClass import DBFunctionsClass

def token_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'Authorization' in request.headers:
            if request.headers['Authorization'].startswith('mini-unsplash '):
                try:
                    token = request.headers['Authorization']
                    jwt_token = token.split('mini-unsplash ')[1]
                    payload = jwt.decode(jwt_token, config.SECRET_KEY, algorithms="HS256")

                    kwargs['username'] = payload['username']
                    return func(*args, **kwargs)
                except jwt.ExpiredSignatureError:
                    return make_response({'message': [] , 'response':'"Token is expired"'}, 401)
                except jwt.InvalidTokenError:
                    return make_response({'message': [], 'response':'Token is invalid'}, 402)
            return make_response({'message': [], 'response':'Token is invalid!'}, 403)
        return make_response({'message': [], 'response':'Token is missing!'}, 401)
    return wrap

def manage_db_connection(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):

        function_return_data = func(*args, **kwargs)

        #MANAGE DATABASE CONNECTION
        DBFunctionsClass.manageDBConnection()

        return function_return_data

    return wrapper_function
