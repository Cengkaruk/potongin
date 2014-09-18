#!/usr/bin/env python

from flask import Blueprint
from app.helpers.RestHelper import RestHelper
from app.decorators.authdecorators import *

#--------------------------------------
# Setup for blueprints
#--------------------------------------
apis = Blueprint('apis', __name__, url_prefix='/api')

#--------------------------------------
# API
#--------------------------------------
@apis.route('/')
@token_required('GET')
def index():
  return RestHelper().build_response(200, 200, {}, 'Ready for resize, crop, and compress your image?')