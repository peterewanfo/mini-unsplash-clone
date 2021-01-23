import time, jwt
import traceback
from config import config

class HelperClass():

    @staticmethod
    def convertDateToTimestamp(str_date):
        """str_date SHOULD BE IN THE FORMAT YYYY-mm-dd"""

        converted_timestamp = 0
        try:

            date_stripped = str(str_date).split('-')
            date_tuple = (int(date_stripped[0]), int(date_stripped[1]), int(date_stripped[2]), 0,0,0,0,0,0)

            converted_timestamp = time.mktime(date_tuple)

        except Exception:
            pass

        return converted_timestamp

    @staticmethod
    def getTimeStampFromYearAndMonth(year, month):
        try:
            
            generated_tuple = (int(year), int(month), 1, 0,0,0,0,0,0 )

            current_time = int(time.time())

            generated_timestamp = int(time.mktime(generated_tuple) )

            return generated_timestamp

        except Exception:
            return False

    @staticmethod
    def getDateFromTimeStamp(timestamp):
        
        converted = str(time.strftime("%A, %d %b %Y", time.localtime(int(timestamp) ) ) )

        return converted

    @staticmethod
    def getDateTimeFromTimeStamp(timestamp):
        
        conveted = str(time.strftime("%A, %d %b %Y, %I:%M%p", time.localtime(int(timestamp) ) ) )

        return converted

    @staticmethod
    def createLoginToken(username):
        #NOTE LOGIN PREDICATE: AfemaiWonderCityManagement

        # creates a dict for access token and refresh token payload 
        rt_payload = {
            'username': username
            # 'exp': int(time.time() + 86400) # expires after 24hrs
        }
        at_payload = {
            'username': username
            # 'exp': int(time.time() + 86400) # expires after 5mins
            # 'exp': int(time.time() + 300) # expires after 5mins
        }
        #creates and return the access and refresh token
        refresh_token = jwt.encode(rt_payload, config.SECRET_KEY).decode("utf-8")
        access_token = jwt.encode(at_payload, config.SECRET_KEY).decode("utf-8")
        return refresh_token, access_token

    @staticmethod
    def correctListForTupleSearch(items_list):

        if len(items_list) == 0:
            items_list.append("NONE")
            items_list.append("NONE")
        if len(items_list) == 1:
            items_list.append("NONE")

        return items_list

    @staticmethod
    def suggestUsernameFromText(from_suggestion_text):
        try:

            import random

            single_text_word = str(from_suggestion_text).split(' ')

            single_text_word = str(single_text_word[0]) + random.randint(121232,999999)

        except Exception:
            return from_suggestion_text

    @staticmethod
    def _encryptText(raw_text):
        """
        Hash text e.g user password
        
        Returns --> False(Boolean) / (String)
                On Error and real data respectively
        """
        try:
            
            import passlib
            from passlib.hash import sha256_crypt
            
            encrypted_text = sha256_crypt.encrypt(raw_text)
            
            return encrypted_text
        
        except Exception:
            print("======ERROR OCCURED WHEN HASHING TEXT=====")
            print(str(traceback.format_exc() ) )
            return False
        
    @staticmethod
    def _decryptText(raw_trial_text, encrypted_hash):
        """Decrupt text e.g user password hash
            Returns --> False(Boolean) / False(Boolean)
        """
        try:
            import passlib
            from passlib.hash import sha256_crypt
            
            decrypted_text = sha256_crypt.verify(raw_trial_text, encrypted_hash)

            return decrypted_text
            
        except Exception:
            print("======AN ERROR OCCURED WHEN DECRYPTING TEXT====")
            print(str(traceback.format_exc()))
            return False
