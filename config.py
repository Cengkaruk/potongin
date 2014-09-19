import os

#--------------------------------------
# Base Config
#--------------------------------------
BASE_URL = 'http://localhost:5000/'
_basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

#--------------------------------------
# Access Token
# Please change this default access token
#--------------------------------------
ACCESS_TOKEN = 'kkdosak994jdu82jdjda0djs9dusa903rjf90sjdoaod'

#--------------------------------------
# Image Storage
#--------------------------------------
UPLOAD_STORAGE = 'public/uploads'
IMAGE_STORAGE = 'public/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])