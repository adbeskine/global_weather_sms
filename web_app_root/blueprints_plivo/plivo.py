from flask import Flask, request, Response, Blueprint
import plivo, plivoxml, requests, sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
from command_functions.commands import command_handler


plivo = Blueprint('plivo', __name__)

@plivo.route('/plivo_sms', methods=['GET', 'POST'])
def plivo_sms():
	from_number = request.values.get('From')
	to_number = request.values.get('To')
	message = request.values.get('Text')
	command = message.split()
	response = command_handler(command)
	params = {
	"src": to_number,
	"dst": from_number,
	}
	body = response

	r = plivoxml.Response()
	r.addMessage(body, **params)
	return Response(str(r), mimetype='text/xml')

	#PLIVO SYSTEM IS AWFUL. BARELY WORKS. TODO: fix this...
