from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def serialize(self):
        return{
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'content': self.content,
            'date_posted': self.date_posted.strftime('%Y-%m-%d %H:%M :%S')
        }