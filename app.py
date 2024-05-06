from models.dbconfig import db
from apis.register_routes import register_routes
# from flask_jwt_extended import JWTManager
from flask import Flask, current_app
from ext import migrate, CORS, socketio, jwt
from config import Config
# from flask_mail import Mail



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    socketio.init_app(app)

    return app

app = create_app()

# server_url = "https://****.onrender.com"

# Initialize JWTManager with the app
jwt.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        register_routes(app, db, socketio)
        socketio.run(app, debug=True, host="0.0.0.0")
        jwt_key = current_app.config['JWT_SECRET_KEY']
        db.create_all()
        print("Initializing Socket.IO server...")
        socketio.init_app(app)
        print("Socket.IO server initialized")
        print("Starting Flask app...")
        app.run(debug=True, host="0.0.0.0")