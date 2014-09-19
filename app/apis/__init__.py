#!/usr/bin/env python

import os
import string
import random
from flask import Blueprint, request, redirect, url_for
from werkzeug import secure_filename

from app.helpers.RestHelper import RestHelper
from app.helpers.ImagickHelper import ImageResizer
from app.decorators.authdecorators import *
from app import app

#--------------------------------------
# Setup for blueprints
#--------------------------------------
apis = Blueprint('apis', __name__, url_prefix='/api')

# Just allow some extentions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

#--------------------------------------
# API
#--------------------------------------
@apis.route('/')
@token_required('GET')
def index():
  return RestHelper().build_response(200, 200, {}, 'Ready for resize, crop, and compress your image?')

@apis.route('/resize', methods=['POST'])
@token_required('POST')
def image_resize():
  file = request.files['image']
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    
    random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

    filename = ''.join([random_name, os.path.splitext(filename)[1]])
    upload_path = os.path.abspath(os.path.join(app.config['UPLOAD_STORAGE'], filename))

    # Save
    file.save(upload_path)

    destination_path = os.path.abspath(os.path.join(app.config['IMAGE_STORAGE'], random_name))
    os.makedirs(destination_path)

    # With compress params?
    if request.form['compress'] == 'true':
      small_240x180 = ImageResizer().resize_image(upload_path, ImageResizer.small_240x180, ImageResizer.small_240x180_name, destination_path, True)
      small_320x240 = ImageResizer().resize_image(upload_path, ImageResizer.small_320x240, ImageResizer.small_320x240_name, destination_path, True)
      medium_640x480 = ImageResizer().resize_image(upload_path, ImageResizer.medium_640x480, ImageResizer.medium_640x480_name, destination_path, True)
      medium_800x600 = ImageResizer().resize_image(upload_path, ImageResizer.medium_800x600, ImageResizer.medium_800x600_name, destination_path, True)
      large_1024x768 = ImageResizer().resize_image(upload_path, ImageResizer.large_1024x768, ImageResizer.large_1024x768_name, destination_path, True)
      large_1600x1200 = ImageResizer().resize_image(upload_path, ImageResizer.large_1600x1200, ImageResizer.large_1600x1200_name, destination_path, True)
    else:
      small_240x180 = ImageResizer().resize_image(upload_path, ImageResizer.small_240x180, ImageResizer.small_240x180_name, destination_path)
      small_320x240 = ImageResizer().resize_image(upload_path, ImageResizer.small_320x240, ImageResizer.small_320x240_name, destination_path)
      medium_640x480 = ImageResizer().resize_image(upload_path, ImageResizer.medium_640x480, ImageResizer.medium_640x480_name, destination_path)
      medium_800x600 = ImageResizer().resize_image(upload_path, ImageResizer.medium_800x600, ImageResizer.medium_800x600_name, destination_path)
      large_1024x768 = ImageResizer().resize_image(upload_path, ImageResizer.large_1024x768, ImageResizer.large_1024x768_name, destination_path)
      large_1600x1200 = ImageResizer().resize_image(upload_path, ImageResizer.large_1600x1200, ImageResizer.large_1600x1200_name, destination_path)

    return_data = {
      'small_240x180': small_240x180,
      'small_320x240': small_320x240,
      'medium_640x480': medium_640x480,
      'medium_800x600': medium_800x600,
      'large_1024x768': large_1024x768,
      'large_1600x1200': large_1600x1200
    }

    return RestHelper().build_response(200, 200, return_data, 'Wohooo, you got many size of your image!')
 
