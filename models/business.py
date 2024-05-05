from models.dbconfig import db 


class Business(db.Model):
    __tablename__ = "business"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    contact = db.Column(db.String(50))
    currency = db.Column(db.String(10))
    country = db.Column(db.String(50))
    users = db.relationship("Users", back_populates="business")

    def __init__(self, name, description, contact, currency, country):
        self.name = name
        self.description = description
        self.contact = contact
        self.currency = currency
        self.country = country

    def __repr__(self):
        return f"<Business {self.id}>"