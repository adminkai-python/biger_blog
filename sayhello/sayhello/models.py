from sayhello import db
from datetime import datetime

class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
    comment = db.Column(db.Text,nullable=False)
    time = db.Column(db.DateTime,default=datetime.utcnow,index=True)


