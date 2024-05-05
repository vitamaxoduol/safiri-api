import os
import dotenv
dotenv.load_dotenv()





class Config:
    # Flask app configurations
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///safiri.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT configurations
    JWT_SECRET_KEY = os.urandom(32).hex()
    JWT_TOKEN_LOCATION = ['headers', 'cookies'] 
    JWT_COOKIE_CSRF_PROTECT = True  # Enable CSRF protection for JWT cookies
    JWT_ACCESS_TOKEN_EXPIRES = 3600 

    # Socket.IO configurations
    SOCKETIO_MESSAGE_QUEUE = 'redis://localhost:6379/0' # Redis message queue for Socket.IO

