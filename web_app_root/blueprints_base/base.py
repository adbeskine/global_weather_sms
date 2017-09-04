from flask import Blueprint

base = Blueprint('base', __name__)

@base.route('/')
def index():
	return 'index.html' #information on how to use the service etc.