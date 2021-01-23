import mysql.connector as MySQLdb
import time
import passlib
from passlib.hash import sha256_crypt

class DBModels():

    db = None
    cursor = None
    database_name = "MiniUnsplashDB"
    database_password = "MiniUnsplashDBPassword"

    can_init_db = False

    @classmethod
    def dbConnect(cls):
        cls.db = MySQLdb.connect(host='localhost', user='root', password=cls.database_password)

        cls.cursor = cls.db.cursor(buffered=True)

        try:
            cls.createTable('DROP DATABASE IF EXISTS SignalAllianceInterview')
            cls.cursor.execute(f'USE {cls.database_name}')

        except Exception:

            cls.createTable('DROP DATABASE IF EXISTS SignalAllianceInterview')

            cls.cursor.execute(f'CREATE DATABASE IF NOT EXISTS {cls.database_name}')

            cls.cursor.execute(f'USE {cls.database_name}')
            
            cls.can_init_db = True

    @classmethod
    def createTable(cls, query):

        cls.cursor.execute(query)
        
        cls.db.commit()

    @classmethod
    def initDatabase(cls):
            
        cls.dbConnect()

        ########################################################
        #--------DATABASE CREATE --------------------#
        ########################################################

        #TABLE TO HOLD USERS RECORD
        cls.createTable("CREATE TABLE IF NOT EXISTS Users("
                    "id INT(11) PRIMARY KEY AUTO_INCREMENT, "
                    "username VARCHAR(100) UNIQUE, "
                    "password MEDIUMTEXT, "
                    "date_created INT(11) "
                    ") ENGINE = InnoDB;")

        #TABLE TO HOLD IMAGES CATEGORY
        cls.createTable("CREATE TABLE IF NOT EXISTS ImagesCategory("
                    "id INT(11) PRIMARY KEY AUTO_INCREMENT, "
                    "category_name VARCHAR(100) UNIQUE, "
                    "date_created INT(11) "
                    ") ENGINE = InnoDB;")

        #TABLE TO HOLD ALL IMAGES
        cls.createTable("CREATE TABLE IF NOT EXISTS Images("
                    "id INT(11) PRIMARY KEY AUTO_INCREMENT, "
                    "image_title MEDIUMTEXT, "
                    "category_id INT(11), "
                    "FOREIGN KEY (category_id) REFERENCES ImagesCategory(id) ON UPDATE CASCADE ON DELETE CASCADE, "
                    "image_tag MEDIUMTEXT, "
                    "img_local_url MEDIUMTEXT, "
                    "cloudinary_url MEDIUMTEXT, "
                    "date_created INT(11) "
                    ") ENGINE = InnoDB;")
