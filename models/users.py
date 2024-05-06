from models.dbconfig import db 
# from models.business import Business

# Users model
class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))  # Store hashed and salted passwords
    role = db.Column(db.Enum("passenger", "business manager", "Intasend admin"))
    phone_number = db.Column(db.String(20))
    business_id = db.Column(db.Integer, db.ForeignKey("business.id"))
    business = db.relationship("Business", back_populates="users")
    payments = db.relationship("Payments", back_populates="user")
    bookings = db.relationship("Bookings", back_populates="user")


    def __init__(self, first_name, last_name, username, email, password_hash, role, phone_number, business_id):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.phone_number = phone_number

    def __repr__(self):
        return f"<User {self.username}>"
    


# Business model
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