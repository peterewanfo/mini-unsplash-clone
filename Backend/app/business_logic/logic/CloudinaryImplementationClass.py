import cloudinary as Cloud
import traceback
import cloudinary.uploader

class CloudinaryImplementation():

    @staticmethod
    def pushToCloud(file, image_name):

        try:

            #THIS SHOULD HAVE BEEN ON ENVIRONMENT VARIABLE IF IT WAS TO BE ON PRODUCTION
            Cloud.config(
                cloud_name = 'peter-cloudinary-cloud',
                api_key = '936933897221485',
                api_secret ='-bLefodiZ-m8KVxYFb0PvL8J3r4',
            )

            resource = Cloud.uploader.upload(file = file, public_id = image_name)

            return resource.url

        except Exception:
            print(traceback.format_exc() )
            return ""

