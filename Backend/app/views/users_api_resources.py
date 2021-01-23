from app.business_logic.utils.Decorators import token_required, manage_db_connection

from config import config

from app.business_logic.utils.HelperClass import HelperClass as UtilsHelperClass

from flask import request, jsonify, make_response, json
import jwt, traceback

from flask_restx import Resource

from app.business_logic.logic.UsersClass import UsersClass

from app.views import users_api_call

from app.api_models.user_models import user_login_model, user_registration_model

@users_api_call.route('/register')
@users_api_call.doc(security=None)
class RegisterUser(Resource):
    @staticmethod
    @manage_db_connection
    @users_api_call.expect(user_registration_model)
    def post():
        try:

            json_data = request.get_json()

            username = json_data["username"]
            password = json_data["password"]

            data = UsersClass.createNewUser(username = username, password = password)

            if data:

                payload = {
                    "username":username
                }

                new_token = jwt.encode(payload, config.SECRET_KEY, algorithm="HS256")

                return make_response(jsonify({
                    'message':new_token,
                    "response":"successful"
                }), 200)

            return make_response(jsonify({'message': False, 'response': 'An Error occured'}), 400)


        except Exception as e:

            print(str(traceback.format_exc() ))

            return make_response(jsonify({"message": False, "response": 'An Error occured ' } ), 400)


@users_api_call.route('/login')
@users_api_call.doc(security=None)
class LoginUser(Resource):
    @staticmethod
    @manage_db_connection
    @users_api_call.expect(user_login_model)
    def post():
        try:

            json_data = request.get_json()

            username = json_data["username"]
            password = json_data["password"]

            data = UsersClass.getUserLoginDetails(username = username)

            if data:

                if UtilsHelperClass._decryptText(raw_trial_text = password, encrypted_hash = data['password']):

                    payload = {
                        "username":username
                    }

                    new_token = jwt.encode(payload, config.SECRET_KEY, algorithm="HS256")

                    return make_response(jsonify({
                        'message':new_token,
                        "response":"successful"
                    }), 200)

            return make_response(jsonify({'message': False, 'response': 'An Error occured'}), 400)


        except Exception as e:

            print(str(traceback.format_exc() ))

            return make_response(jsonify({"message": False, "response": 'An Error occured ' } ), 400)

