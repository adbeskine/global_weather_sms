from web_app_root import db

class commands(db.Model):

	__tablename__ = "commands"

	Id = db.Column(db.Integer, primary_key=True)
	command = db.Column(db.String)
	time = db.Column(db.Time)
	number = db.Column(db.String)

	def __init__(self, c1, c2, c3, c4, c5):
		self.command = command
		self.time = time
		self.number = number

	def __repr__(self):
		return 'command = {} {} {}'.format(command, number, time)

