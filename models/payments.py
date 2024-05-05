from models.dbconfig import db


class Payments(db.Model):
    __tablename__ = "payments"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    amount = db.Column(db.Float)
    payment_method = db.Column(db.String(50))
    timestamp = db.Column(db.String(50))
    user = db.relationship("Users", back_populates="payments")

    def __init__(self, user_id, amount, payment_method, timestamp):
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.timestamp = timestamp

    def __repr__(self):
        return f"<Payment {self.id}>"