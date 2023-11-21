from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Create a users table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id as primary key
    name = db.Column(db.String(50), nullable=False) # username

    def __repr__(self):
        return "<User: {}>".format(self.name)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    