from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)
    role = db.Column(db.String(50), nullable=False)
