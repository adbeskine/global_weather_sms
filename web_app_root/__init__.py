from flask import Flask
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..' ))

app = Flask(__name__)

from web_app_root.blueprints_base.base import base
from web_app_root.blueprints_twilio.twilio import twilio #rename this properly 

app.register_blueprint(base)
app.register_blueprint(twilio)