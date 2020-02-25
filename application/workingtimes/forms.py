from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import validators

#def validate_date(date):
#    if date < timezone.now().date():
#        raise ValidationError("Date cannot be in the past")

class WorkingtimesForm(FlaskForm):
    time = DateField("Date")
 
    class Meta:
        csrf = False
