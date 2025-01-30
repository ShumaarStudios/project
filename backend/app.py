from flask import Flask
from flask_cors import CORS
from models.user import User
from models.extracts import Extract
from models.soil_data import SoilData
from routes.auth import auth_bp
from routes.recommendation import recommendation_bp
from routes.image_recognition import image_recognition_bp
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(recommendation_bp, url_prefix='/api/recommendation')
app.register_blueprint(image_recognition_bp, url_prefix='/api/image')

if __name__ == '__main__':
    app.run(debug=True)
