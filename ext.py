from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager


migrate = Migrate()
socketio = SocketIO(cors_allowed_origins="*")
jwt = JWTManager()