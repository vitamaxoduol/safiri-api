from models.dbconfig import db 


class Vehicles(db.Model):
    __tablename__ = "vehicles"
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(20))
    vehicle_type = db.Column(db.String(50))
    current_location = db.Column(db.String(100))
    status = db.Column(db.String(20))
    bookings = db.relationship("Bookings", back_populates="vehicle")
    routes = db.relationship("Routes", secondary="bookings", backref="vehicles")

    def __init__(self, vehicle_number, vehicle_type, current_location, status):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.current_location = current_location
        self.status = status

    def __repr__(self):
        return f"<Vehicle {self.id}>"