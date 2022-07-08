from flask import Flask
from flask_restful import Api
from anlat_rest_api.endpoints.index import Index
from anlat_rest_api.endpoints.auth import Auth

import datetime
import os
from flask import render_template
from flask import Flask
# from turkgeckorestapi.config import init_config
app = Flask(__name__)
# init_config(app)
api = Api(app)

# print(app.config)
api.add_resource(Index, '/')
api.add_resource(Auth, '/auth')

