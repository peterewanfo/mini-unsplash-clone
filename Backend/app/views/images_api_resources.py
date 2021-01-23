from app.business_logic.utils.Decorators import token_required, manage_db_connection

from app.business_logic.utils.LocalFileUploader import LocalFileUploader

from app.business_logic.utils.HelperClass import HelperClass as UtilsHelperClass

from flask import request, jsonify, make_response, json, url_for
import jwt, traceback, time, datetime

from app.business_logic.utils.Constants import Constants
Constants = Constants()

from flask_restx import Resource

from app.business_logic.logic.ImagesClass import ImagesClass

from app.views import images_api_call

from app.api_models.images_models import new_category_model, new_images_model

@images_api_call.route('/new-category')
class NewCategory(Resource):
    @staticmethod
    @token_required
    @manage_db_connection
    @images_api_call.expect(new_category_model)
    def post(username):
        try:

            json_data = request.get_json()

            category_name = json_data["category_name"]

            data = ImagesClass.createNewCategory(category_name = category_name)

            return jsonify({'message': data, 'response': 'Success'})


        except Exception as e:

            print(str(traceback.format_exc() ))

            return make_response(jsonify({"message": False, "response": 'An Error occured ' } ), 400)


@images_api_call.route('/fetch-categories')
class AllCategories(Resource):
    @staticmethod
    @token_required
    @manage_db_connection
    def get(username):
        try:

            data = ImagesClass.fetchCategories()

            return jsonify({'message': data, 'response': 'Success'})


        except Exception as e:

            print(str(traceback.format_exc() ))

            return make_response(jsonify({"message": False, "response": 'An Error occured ' } ), 400)


@images_api_call.route('/filter-images')
class FilterImages(Resource):
    @staticmethod
    @token_required
    @manage_db_connection
    @images_api_call.param("by_tag_name")
    @images_api_call.param("by_category_name")
    def get(username):
        try:

            by_tag_name = ""
            by_category_name = ""

            try:
                by_tag_name = request.args["by_tag_name"]
            except Exception:
                pass
            try:
                by_category_name = request.args["by_category_name"]
            except Exception:
                pass

            if by_tag_name == "":
                by_tag_name = False
            if by_category_name == "":
                by_category_name = False

            data = ImagesClass.filterImages(by_tag_name = by_tag_name, by_category_name = by_category_name)

            return jsonify({'message': data, 'response': 'Success'})


        except Exception as e:

            print(str(traceback.format_exc() ))

            return make_response(jsonify({"message": False, "response": 'An Error occured ' } ), 400)


@images_api_call.route('/add')
class AddImages(Resource):
    @staticmethod
    @token_required
    @manage_db_connection
    @images_api_call.expect(new_images_model)
    def post(username):
        try:

            image_title = request.form["image_title"]
            image_tag = request.form["image_tag"]
            category_id = request.form["category_id"]
            upload_to_cloudinary = request.form["upload_to_cloudinary"]

            img_url = False
            try:
                img_url = request.files["file"]
            except Exception:
                print(traceback.format_exc() )
                pass

            if category_id == "":
                category_id = False

            #SEND FILE TO UPLOADER
            file_upload_folder = Constants.content_upload_folders[0]

            #UPLOAD IMAGE TO LOCAL STORAGE
            upload_data = LocalFileUploader.uploadToLocalDirectory(file = img_url, file_upload_folder = file_upload_folder)

            #UPLOAD DATA TO DATABASE
            data = ImagesClass.addNewImage(image_title = image_title, image_tag = image_tag, img_local_url = upload_data["new_filename"], cloudinary_url = "" , category_id = category_id)

            if upload_to_cloudinary and data:
                #PUSH FILE TO CLOUD
                from app.business_logic.logic.CloudinaryImplementationClass import CloudinaryImplementation

                cloudinary_url = CloudinaryImplementation.pushToCloud(file = img_url, image_name = upload_data["new_filename"] )

                #UPDATE CLOUDINARY URL TO IMAGE IN DATABASE AFTER SUCCESSFUL UPLOAD

                ImagesClass.updateImageCloudinaryUrl(cloudinary_url = cloudinary_url, image_id = data)

            return jsonify({'message': bool(data), 'response': 'Success'})

        except Exception as e:

            print(str(traceback.format_exc() ))

            return make_response(jsonify({"message": False, "response": 'An Error occured ' } ), 400)
