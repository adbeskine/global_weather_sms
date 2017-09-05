from flask import Blueprint, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..' ))
from command_functions.commands import command_handler
from web_app_root import db
from web_app_root.models import commands

twilio = Blueprint('twilio', __name__)

@twilio.route('/twilio_sms', methods=['GET', 'POST'])
def twilio_sms():
	message = request.form['Body']
	number = request.form['From']
	command = message.split()
	response = command_handler(command, number)
	resp = MessagingResponse()
	response = response + '   - you are receiving this alert through the twilio api by Alexander Beskine'
	resp.message(str(response)) #generated in commands #TODO can I remove the str() here?
	return str(resp)



