from models.dbconfig import db 


class Bookings(db.Model):
    __tablename__ = "bookings"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"))
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"))
    subroute_id = db.Column(db.Integer, db.ForeignKey("subroutes.id")) 
    amount = db.Column(db.Float)

    user = db.relationship("Users", back_populates="bookings")
    vehicle = db.relationship("Vehicles", back_populates="bookings")
    route = db.relationship("Routes", back_populates="bookings")
    subroute = db.relationship("Subroutes", back_populates="bookings")

    def __init__(self, user_id, vehicle_id, route_id, subroute_id, amount):  # Updated constructor
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.route_id = route_id
        self.subroute_id = subroute_id
        self.amount = amount

    def __repr__(self):
        return f"<Booking {self.id}>"