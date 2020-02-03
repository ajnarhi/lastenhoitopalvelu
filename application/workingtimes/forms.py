from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField

class WorkingtimesForm(FlaskForm):
    time = DateField("Date")
 
    class Meta:
        csrf = False
