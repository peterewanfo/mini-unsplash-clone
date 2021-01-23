import sys
import os
import time
import traceback
from config import basedir

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from app.business_logic.utils.Constants import Constants

class BaseClass(Constants):

	def __init__(self):

		Constants.__init__(self)

		self.all_allowed_extension = ['jpg', 'png', 'jpeg']

		self.upload_destination = '/'.join([basedir, 'app/static/other_images'])

		self.destination = '/'.join([basedir, 'app/static/other_images'])

		self.my_upload_target = ""

	def _isAllowedFile(self, filename):

		self.file_extension = str(filename.split('.')[1]).lower()

		return '.' in filename and (str(filename.split('.')[1])).lower() in self.all_allowed_extension

	def _createUploadFolder(self, upload_folder_name, filename):
		try:
			
			self._isAllowedFile(filename = str(filename) )
			file_extension = self.file_extension

			if file_extension == 'jpg' or file_extension == 'png' or file_extension == 'jpeg':

				my_pictures = '/' .join([self.upload_destination, upload_folder_name ] )
				if not os.path.isdir(my_pictures):
					os.mkdir(my_pictures)

				self.my_upload_target = '/'.join([my_pictures, filename])
				return True
				
			elif file_extension == 'mp4' or file_extension == 'mp3' or file_extension == 'pdf' or file_extension == 'xlsx' :
				
				my_file = '/' .join([self.upload_destination,str(upload_folder_name) ])
				
				if not self.os.path.isdir(my_file):
					self.os.mkdir(my_file)

				self.my_upload_target = '/'.join([my_file, filename])
				return True
				
			else:
				return False

		except Exception:
			return False

	def _checkFileStaticDirectory(self, filename, folder_name):
		if filename in self.default_img_resources:
			directory = str(self.IP_ADDRESS) +"/static/" + "default/" + str(filename)
			return directory
		else:
			if filename != "none" and filename != "unknown":
				directory = str(self.IP_ADDRESS) +"/static/" + "other_images/" +str(folder_name) +"/" + str(filename)
				return directory
			else:
				directory = str(self.IP_ADDRESS) +"/static/" + "default/" + "profile_photo.png"
				return directory