from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class NannyForm(FlaskForm):
    name = StringField("Nanny name", [validators.Length(min=2,max=15, message='Name must be 2-15 characters')])
    age = IntegerField("Nanny age", [validators.NumberRange(min=18, max=100, message='Nanny must be 18 to 100 years old')])
    phonenumber = IntegerField("Nanny phonenumber", [validators.NumberRange(min=1000000,max=1000000000,message='Phonenumber must be seven to ten numbers')])

    class Meta:
        csrf = False
