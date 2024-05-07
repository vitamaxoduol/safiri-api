from models.dbconfig import db 


class Routes(db.Model):
    __tablename__ = "routes"
    
    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(100))
    stop_location = db.Column(db.String(100))
    duration = db.Column(db.String(50))
    amount= db.Column(db.Float)
    

    def __init__(self, start_location, stop_location, duration, amount):
        self.start_location = start_location
        self.stop_location = stop_location
        self.duration = duration
        self.amount = amount

    def __repr__(self):
        return f"<Route {self.id}>"




class SubRoutes(db.Model):
    __tablename__ = "subroutes"

    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(100))
    stop_location = db.Column(db.String(100))
    duration = db.Column(db.String(50))
    amount = db.Column(db.Float)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"))

    route = db.relationship("Routes", back_populates="subroutes")

    def __init__(self, start_location, stop_location, duration, amount):
        self.start_location = start_location
        self.stop_location = stop_location
        self.duration = duration
        self.amount = amount

    def __repr__(self):
        return f"<SubRoute {self.id}>"