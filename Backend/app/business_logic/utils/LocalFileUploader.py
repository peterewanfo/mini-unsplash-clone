import time
import traceback
from PIL import Image

class LocalFileUploader():

    @staticmethod
    def uploadToLocalDirectory(file, file_upload_folder):
        try:

            if file:

                from app.business_logic.utils.BaseClass import BaseClass
                BaseClass = BaseClass()

                allowed_file = BaseClass._isAllowedFile(filename = str(file.filename) )
                file_item_is = BaseClass.file_extension

                data = {
                    "new_filename":"None",
                    "target":"None",
                    "height":"0",
                    "width":"0"
                }

                if allowed_file:

                    current_time = int(time.time())

                    new_filename = str(file_upload_folder).replace(" ", "_") + "_file_" + str(current_time)  + "." + str(file_item_is)

                    is_created = BaseClass._createUploadFolder(upload_folder_name = file_upload_folder, filename = str(new_filename) )

                    target = BaseClass.my_upload_target

                    #SAVE THE IMAGE TO THE DATABASE
                    #THIS CAN BE SENT TO AWS SERVER
                    file.save(target)

                    #GET UPLOADED IMAGE SIZE
                    im = Image.open(target)
                    original_width, original_height = im.size

                    #GET IMAGE SIZES
                    sizes = BaseClass.image_sizes

                    for size in sizes:

                        im = Image.open(target)
                        
                        im.thumbnail(size, Image.ANTIALIAS )

                        new_filename = str(file_upload_folder).replace(" ", "_") + "_file_" + str(current_time) +"_" + str(size[0]) +"_"+ str(size[1]) + "." + str(file_item_is)

                        is_created = BaseClass._createUploadFolder(upload_folder_name = file_upload_folder, filename = str(new_filename) )

                        resized_target = BaseClass.my_upload_target

                        im.save(resized_target)

                    data = {
                        "new_filename":new_filename,
                        "target":target,
                        "height":original_height,
                        "width":original_width
                    }

                    return data
                return data
            data = {
                "new_filename":"None",
                "target":"None",
                "height":"0",
                "width":"0"
            }

            return data

        except Exception:
            print(str(traceback.format_exc() ))
            data = {
                "new_filename":"None",
                "target":"None",
                "height":"0",
                "width":"0"
            }

            return data