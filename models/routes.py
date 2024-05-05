from models.dbconfig import db 


class Routes(db.Model):
    __tablename__ = "routes"
    
    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(100))
    stop_location = db.Column(db.String(100))
    duration = db.Column(db.String(50))
    fare = db.Column(db.Float)
    route_transactions = db.relationship("RouteTransactions", back_populates="route")

    def __init__(self, start_location, stop_location, duration, fare):
        self.start_location = start_location
        self.stop_location = stop_location
        self.duration = duration
        self.fare = fare

    def __repr__(self):
        return f"<Route {self.id}>"