from application import db
from application.models import Base

from sqlalchemy.sql import text
from flask_login import  current_user

class Nanny(Base):

    name = db.Column(db.String(144), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)

    agency = db.relationship("AgencyNanny", backref='nanny', lazy=True)

    workingtimes = db.relationship("Workingtimes", backref='workingtimes', lazy=True)

    def __init__(self, name, age, phonenumber):
        self.name = name
        self.age = age
        self.phonenumber = phonenumber

    @staticmethod
    def find_nannies_with_workingtimes():
        stmt = text("SELECT Nanny.id, Nanny.name FROM Nanny"
                    " LEFT JOIN Workingtimes ON workingtimes.nanny_id = nanny.id"
                    " WHERE NOT Workingtimes.reserved"
                    " GROUP BY Nanny.id"
                    " HAVING COUNT(Workingtimes.id) > 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response


    @staticmethod
    def find_nanny_with_most_workingtimes_in_all_agencys():
        stmt = text("SELECT Nanny.id, Nanny.name, count(workingtimes.id) AS workingtimesamount FROM Nanny"
                    " LEFT JOIN Workingtimes ON workingtimes.nanny_id = nanny.id"
                    " WHERE NOT Workingtimes.reserved"
                    " GROUP BY Nanny.id" 
                    " HAVING COUNT(Workingtimes.id) > 0"
                    " ORDER BY workingtimesamount DESC LIMIT 1")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "workingtimeamount":row[2]})

        return response


    @staticmethod
    def find_nanny_with_most_workingtimes_in_current_agency():
        stmt = text("SELECT Nanny.id, Nanny.name, count(workingtimes.id) AS workingtimesamount FROM Nanny"
                    " LEFT JOIN Workingtimes ON workingtimes.nanny_id = nanny.id"
                    " JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user"
                    " WHERE NOT Workingtimes.reserved"
                    " GROUP BY Nanny.id" 
                    " HAVING COUNT(Workingtimes.id) > 0"
                    " ORDER BY workingtimesamount DESC LIMIT 1").params(c_user=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "workingtimeamount":row[2]})

        return response

    @staticmethod
    def find_nanny_with_most_reservation_in_agency():
        stmt = text("SELECT Nanny.id, Nanny.name, count(workingtimes.id) AS workingtimesamount FROM Nanny"
                    " LEFT JOIN Workingtimes ON workingtimes.nanny_id = nanny.id"
                    " JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user"
                    " WHERE Workingtimes.reserved"
                    " GROUP BY Nanny.id" 
                    " HAVING COUNT(Workingtimes.id) > 0"
                    " ORDER BY workingtimesamount DESC LIMIT 1").params(c_user=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "workingtimeamount":row[2]})

        return response


        