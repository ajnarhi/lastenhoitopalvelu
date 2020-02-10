from application import db
from application.models import Base

class User(Base):

    __tablename__ = "nannyagency"
  
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    nannies = db.relationship("NannyAgencyNanny", backref='nannyagencynanny', lazy=True)
    
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


class NannyAgencyNanny(Base):

    __tablename__ = "nannyagencynanny"

    nannyagency_id = db.Column(db.Integer, db.ForeignKey('nannyagency.id'),
                           nullable=False)
  
    nanny_id = db.Column(db.Integer, db.ForeignKey('nanny.id'),
                           nullable=False)
    
    def __init__(self, nannyagency_id, nanny_id):
        self.nannyagency_id = nannyagency_id
        self.nanny_id = nanny_id
        