from models.dbconfig import db 


class RouteTransactions(db.Model):
    __tablename__ = "route_transactions"
    
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"))
    total_amounts = db.Column(db.Float)
    last_updated = db.Column(db.String(50))
    route = db.relationship("Routes", back_populates="route_transactions")

    def __init__(self, route_id, total_amounts, last_updated):
        self.route_id = route_id
        self.total_amounts = total_amounts
        self.last_updated = last_updated

    def __repr__(self):
        return f"<RouteTransaction {self.id}>"