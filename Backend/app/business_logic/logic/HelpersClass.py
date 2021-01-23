import traceback
import time
import datetime
import uuid

from app.business_logic.utils.DBFunctionsClass import DBFunctionsClass

class HelpersClass():
    
    @staticmethod
    def isUsernameValid(username):

        try:

            query = f"""SELECT username FROM Users WHERE username = '{username}'"""

            data = DBFunctionsClass.execFetchOne(query)

            if data:

                return True
            else:
                return False

        except Exception:
            return False