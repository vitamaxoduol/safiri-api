from models.dbconfig import db 

# Transactions Model
class Transactions(db.Model):
    __tablename__ = "transactions"
    
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey("payments.id"))  # Foreign key referencing Payments table
    phone_number = db.Column(db.Integer)
    # booking_id = db.Column(db.Integer, db.ForeignKey("bookings.id"))
    amount = db.Column(db.Float)
    status = db.Column(db.Enum("pending", "successful", "failed"))
    reference_code = db.Column(db.String(15))
    timestamp = db.Column(db.String(50))

    def __init__(self, payment_id, booking_id, amount, timestamp):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.amount = amount
        self.timestamp = timestamp


# Payments Model
class Payments(db.Model):
    __tablename__ = "payments"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    amount = db.Column(db.Float)
    reference_code = db.Column(db.String(15))
    payment_method = db.Column(db.Enum("MPESA", "Bank")) # MPESA, bank 
    internal_reference = db.Column(db.String(15))
    timestamp = db.Column(db.String(50))
    # Define relationship with Transactions
    transactions = db.relationship("Transactions", backref="payment")  # Relationship defined here

    def __init__(self, user_id, amount, payment_method, internal_reference, timestamp):
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.internal_reference = internal_reference
        self.timestamp = timestamp

# Payout Details 
class PayoutDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preferred_option = db.Column(db.Enum("MPESA", "bank"))
    mpesa_reference = db.Column(db.Enum("Paybill", "Till Number"))
    bank_code = db.Column(db.Integer, db.ForeignKey("business.id"))

    def __init__(self, preffered_option, mpesa_reference, bank_code):
        self.preffered_option = preffered_option
        self.mpesa_reference = mpesa_reference
        self.bank_code = bank_code

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

    # Relationships
    business = db.relationship("Business", back_populates="users")
    payments = db.relationship("Payments", backref="user_relation")
    bookings = db.relationship("Bookings", back_populates="user")

    def __init__(self, first_name, last_name, username, email, password_hash, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password_hash = password_hash
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

    # Relationships
    users = db.relationship("Users", back_populates="business")

    def __init__(self, name, description, contact, currency, country):
        self.name = name
        self.description = description
        self.contact = contact
        self.currency = currency
        self.country = country

    def __repr__(self):
        return f"<Business {self.id}>"
    
# Route Models 
class Routes(db.Model):
    __tablename__ = "routes"
    
    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(100))
    stop_location = db.Column(db.String(100))
    duration = db.Column(db.String(50))
    amount = db.Column(db.Float)
    
    def __init__(self, start_location, stop_location, duration, amount):
        self.start_location = start_location
        self.stop_location = stop_location
        self.duration = duration
        self.amount = amount

    def __repr__(self):
        return f"<Route {self.id}>"
    
# Vehicles Model 
class Vehicles(db.Model):
    __tablename__ = "vehicles"
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(20))
    vehicle_type = db.Column(db.String(50))
    current_location = db.Column(db.String(100))
    status = db.Column(db.String(20))
    transaction_id = db.Column(db.Integer, db.ForeignKey("transactions.id"))

    transactions = db.relationship("Transactions", backref="vehicle", foreign_keys=[transaction_id])
    associated_bookings = db.relationship("Bookings", back_populates="vehicle", overlaps="routes,vehicles")
    routes = db.relationship("Routes", secondary="bookings", backref="vehicles", overlaps="routes,vehicles")

    def __init__(self, vehicle_number, vehicle_type, current_location, status):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.current_location = current_location
        self.status = status

    def __repr__(self):
        return f"<Vehicle {self.id}>"

# Bookings Model 
class Bookings(db.Model):
    __tablename__ = "bookings"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"))
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"))
    amount = db.Column(db.Float)
    transaction_id = db.Column(db.Integer, db.ForeignKey("transactions.id"))

    # Relationships
    user = db.relationship("Users", back_populates="bookings", overlaps="routes,vehicles")
    vehicle = db.relationship("Vehicles", back_populates="associated_bookings", overlaps="routes,vehicles")
    route = db.relationship("Routes", backref="bookings", overlaps="routes,vehicles")
    transactions = db.relationship("Transactions", backref="booking")

    def __init__(self, user_id, vehicle_id, route_id, subroute_id, amount):  
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.route_id = route_id
        self.subroute_id = subroute_id
        self.amount = amount

    def __repr__(self):
        return f"<Booking {self.id}>"
    



    # Subroutes Model 
# class SubRoutes(db.Model):
#     __tablename__ = "subroutes"

#     id = db.Column(db.Integer, primary_key=True)
#     start_location = db.Column(db.String(100))
#     stop_location = db.Column(db.String(100))
#     duration = db.Column(db.String(50))
#     amount = db.Column(db.Float)
#     route_id = db.Column(db.Integer, db.ForeignKey("routes.id"))

#     route = db.relationship("Routes", backref="subroutes", foreign_keys=[route_id])

#     def __init__(self, start_location, stop_location, duration, amount):
#         self.start_location = start_location
#         self.stop_location = stop_location
#         self.duration = duration
#         self.amount = amount

#     def __repr__(self):
#         return f"<SubRoute {self.id}>"




    
