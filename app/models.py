from app import db
from datetime import datetime

class Subscription(db.Model):
    id=db.Column(db.integer,primary_key=True)
    email=db.Column(db.String(255),unique=True,nullable=False)
    subscribed_at=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    