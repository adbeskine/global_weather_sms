from web_app_root import db

class commands(db.Model):

	__tablename__ = "commands"

	Id = db.Column(db.Integer, primary_key=True)
	c1 = db.Column(db.String)
	c2 = db.Column(db.String)
	c3 = db.Column(db.String)
	c4 = db.Column(db.String)
	c5 = db.Column(db.String)
	time = db.Column(db.Time)

	def __init__(self, c1, c2, c3, c4, c5):
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		self.c4 = c4
		self.c5 = c5

	def __repr__(self):
		return 'command = {} {} {} {} {} {}'.format(c1, c2, c3, c4, c5, c6)

