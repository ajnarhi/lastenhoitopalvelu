from application import db
from application.models import Base
from sqlalchemy.sql import text
from flask_login import  current_user

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


    @staticmethod
    def find_all_freetimes_agency():
        stmt = text("SELECT COUNT(Workingtimes.id) FROM Workingtimes"
                    " LEFT JOIN Nanny ON workingtimes.nanny_id = nanny.id"
                    " JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user"
                    " WHERE NOT Workingtimes.reserved").params(c_user=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0]})

        return response


    @staticmethod
    def find_all_reserved_agency():
        stmt = text("SELECT COUNT(Workingtimes.id) FROM Workingtimes"
                    " LEFT JOIN Nanny ON workingtimes.nanny_id = nanny.id"
                    " JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user"
                    " WHERE Workingtimes.reserved").params(c_user=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0]})

        return response