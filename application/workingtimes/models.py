from application import db
from application.models import Base

class Workingtimes(Base):

    __tablename__ = "workingtimes"

    time = db.Column(db.DateTime)
    reserved = db.Column(db.Boolean, nullable=False, default=False)
    nanny_id = db.Column(db.Integer, db.ForeignKey('nanny.id'),
                           nullable=False)

    def __init__(self,time,reserved,nanny_id):
       self.time =time
       self.reserved = False
       self.nanny_id=nanny_id
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
