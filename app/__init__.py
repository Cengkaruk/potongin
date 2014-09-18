#!/usr/bin/env python

from flask import Flask
from app.helpers.RestHelper import RestHelper

#--------------------------------------
# App Config
#--------------------------------------
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('application.cfg', silent=True)

#--------------------------------------
# Setup for blueprints
#--------------------------------------
from app.apis import apis

app.register_blueprint(apis)

@app.route('/', methods=['GET'])
def index():
  return RestHelper().build_response(200, 200, {}, 'Potongin.')
  
application = app