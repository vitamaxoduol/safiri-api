
from apis.authentication import  auth_routes



def register_routes(app, db, socketio):

    @app.route("/", methods=["GET"])
    def welcome():
        return "Welcome to Safiri API."
    


    auth_routes(app, db)