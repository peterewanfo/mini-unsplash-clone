import traceback
import time
import datetime

from app.business_logic.utils.DBFunctionsClass import DBFunctionsClass

from app.business_logic.utils.BaseClass import BaseClass
BaseClass = BaseClass()

from app.business_logic.utils.HelperClass import HelperClass as UtilsHelperClass
from app.business_logic.logic.HelpersClass import HelpersClass as LogicHelperClass

class ImagesClass():

    @staticmethod
    def createNewCategory(category_name):

        try:

            current_date = int(time.time())

            query = f"""INSERT INTO ImagesCategory(category_name, date_created 
            ) VALUES (
            '{category_name}', '{current_date}') """

            DBFunctionsClass.execCommitDb(query)
            
            return True

        except Exception:
            print(str(traceback.format_exc() ))
            return False


    @staticmethod
    def fetchCategories():
        try:

            query = f"SELECT * FROM ImagesCategory"

            data = DBFunctionsClass.execFetchAll(query)

            return data
        
        except Exception:
            print(str(traceback.format_exc() ))
            return False

    @staticmethod
    def filterImages(by_tag_name = False, by_category_name = False):
        try:

            query = ""

            if by_tag_name:
                query = f"""SELECT Images.* 
                FROM Images 
                WHERE Images.image_tag = '{by_tag_name}' """

            elif by_category_name:
                query = f"""SELECT Images.* 
                FROM Images 
                INNER JOIN ImagesCategory ON ImagesCategory.id = Images.category_id 
                WHERE ImagesCategory.id = '{by_category_name}'"""

            else:
                query = f"SELECT Images.* FROM Images"

            data = DBFunctionsClass.execFetchAll(query)

            from app.business_logic.utils.Constants import Constants
            Constants = Constants()

            for d in data:

                file_upload_folder = Constants.content_upload_folders[0]

                d["img_local_url"] = BaseClass._checkFileStaticDirectory(d['img_local_url'], file_upload_folder)


            return data
            
        except Exception:
            print(str(traceback.format_exc() ))
            return False

    @staticmethod
    def addNewImage(image_title, image_tag, img_local_url, cloudinary_url, category_id = False):
        try:

            #HANDLE INVALID CATEGORY ID
            category_id = int(category_id)

            current_date = int(time.time() )

            query = f"""INSERT INTO Images(
                image_title, category_id, image_tag, img_local_url, cloudinary_url, date_created
                )VALUES(
                    '{image_title}', '{category_id}', '{image_tag}', '{img_local_url}', '{cloudinary_url}', '{current_date}'
                ) """

            DBFunctionsClass.execCommitDb(query)

            #GET IMAGE ID OF CURRENTLY ADDED IMAGE
            query = f"""SELECT id 
                FROM Images 
                WHERE image_tag = '{image_tag}' AND image_title = '{image_title}' AND date_created = '{current_date}' """

            data = DBFunctionsClass.execFetchOne(query)["id"]

            return data

        except Exception:

            print(str(traceback.format_exc() ))
            return False

    @staticmethod
    def updateImageCloudinaryUrl(cloudinary_url, image_id):
        try:

            query = f"""UPDATE Images 
                SET cloudinary_url = '{cloudinary_url}' 
                WHERE id = '{image_id}' """

            DBFunctionsClass.execCommitDb(query)

            return True

        except Exception:
            print(str(traceback.format_exc() ))
            return False