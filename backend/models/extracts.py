from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Extract(db.Model):
    __tablename__ = 'extracts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    application_method = db.Column(db.String(50), nullable=False)
    effectiveness_score = db.Column(db.Float, nullable=False)
    availability = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
