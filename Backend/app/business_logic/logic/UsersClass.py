import traceback
import time
import datetime

from app.business_logic.utils.DBFunctionsClass import DBFunctionsClass

from app.business_logic.utils.HelperClass import HelperClass as UtilsHelperClass
from app.business_logic.logic.HelpersClass import HelpersClass as LogicHelperClass

class UsersClass():

    @staticmethod
    def createNewUser(username, password):

        try:

            current_date = int(time.time())

            is_username_valid = LogicHelperClass.isUsernameValid(username = username)

            #ENCRYPT PASSWORD

            encrypted_password = UtilsHelperClass._encryptText(raw_text = password)

            if not is_username_valid:

                #CREATE NEW USER

                query = f"""INSERT INTO Users(
                    username, password)
                    VALUES(
                    '{username}', '{encrypted_password}')"""

                DBFunctionsClass.execCommitDb(query)

                return True

            else:
                return False

        except Exception:
            print(str(traceback.format_exc() ))
            return False

    @staticmethod
    def getUserLoginDetails(username):
        try:

            query = f"""SELECT username, password 
            FROM Users 
            WHERE username = '{username}'"""

            data = DBFunctionsClass.execFetchOne(query)

            return data

        except Exception:
            return False