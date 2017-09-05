from web_app_root import db
from web_app_root.models import commands

db.create_all()
db.session.commit()