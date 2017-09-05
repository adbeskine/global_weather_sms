from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..' ))

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_pyfile('_config.py')

from web_app_root.blueprints_base.base import base
from web_app_root.blueprints_twilio.twilio import twilio #rename web_app_root properly 
from web_app_root.blueprints_plivo.plivo import plivo

app.register_blueprint(base)
app.register_blueprint(twilio)
app.register_blueprint(plivo)