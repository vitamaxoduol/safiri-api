from models.dbconfig import db

class Transactions(db.Model):
    __tablename__ = "transactions"
    
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey("payments.id"))
    phone_number = db.Column(db.Integer)
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.id"))
    amount = db.Column(db.Float)
    status = db.Column(db.Enum("pending", "successful", "failed"))
    reference_code = db.Column(db.String(15))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"))
    timestamp = db.Column(db.String(50))
    payment = db.relationship("Payments", back_populates="transactions")
    booking = db.relationship("Bookings", back_populates="transactions")
    vehicle = db.relationship("Vehicles", back_populates="transactions")

    def __init__(self, payment_id, booking_id, amount, timestamp):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.amount = amount
        self.timestamp = timestamp