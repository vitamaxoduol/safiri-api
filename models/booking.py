from models.dbconfig import db 


class Bookings(db.Model):
    __tablename__ = "bookings"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"))
    start_location = db.Column(db.String(100))
    stopping_location = db.Column(db.String(100))
    amount = db.Column(db.Float)
    user = db.relationship("Users", back_populates="bookings")
    vehicle = db.relationship("Vehicles", back_populates="bookings")

    def __init__(self, user_id, vehicle_id, start_location, stopping_location, amount):
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.start_location = start_location
        self.stopping_location = stopping_location
        self.amount = amount

    def __repr__(self):
        return f"<Booking {self.id}>"