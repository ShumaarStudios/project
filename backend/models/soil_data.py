from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SoilData(db.Model):
    __tablename__ = 'soil_data'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    soil_type = db.Column(db.String(50), nullable=False)
    ph_level = db.Column(db.Float, nullable=False)
    moisture_level = db.Column(db.Float, nullable=False)
    texture = db.Column(db.String(50), nullable=False)
