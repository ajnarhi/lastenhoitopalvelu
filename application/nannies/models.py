from application import db
from application.models import Base

from sqlalchemy.sql import text

class Nanny(Base):

    name = db.Column(db.String(144), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

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
