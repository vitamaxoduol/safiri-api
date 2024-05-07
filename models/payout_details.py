from models.dbconfig import db 

class PayoutDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preferred_option = db.Column(db.Enum("MPESA", "bank"))
    mpesa_reference = db.Column(db.Enum("Paybill", "Till Number"))
    bank_code = db.Column(db.Integer, db.ForeignKey("business.id"))

    def __init__(self, preffered_option, mpesa_reference, bank_code):
        self.preffered_option = preffered_option
        self.mpesa_reference = mpesa_reference
        self.bank_code = bank_code