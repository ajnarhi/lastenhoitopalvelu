from application import db
from application.models import Base

class Agency(Base):

    __tablename__ = "agency"
  
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    nannies = db.relationship("AgencyNanny", backref='agencynanny', lazy=True)
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]


class AgencyNanny(Base):

    __tablename__ = "agencynanny"

    agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'),
                           nullable=False)
  
    nanny_id = db.Column(db.Integer, db.ForeignKey('nanny.id'),
                           nullable=False)
    
    def __init__(self, agency_id, nanny_id):
        self.agency_id = agency_id
        self.nanny_id = nanny_id
        