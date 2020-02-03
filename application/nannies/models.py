from application import db
from application.models import Base

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

