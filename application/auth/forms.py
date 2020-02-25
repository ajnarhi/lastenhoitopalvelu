from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username",[validators.Length(min=2,max=15, message='Agencys username must be 2-15 characters')])
    password = PasswordField("Password",[validators.Length(min=2,max=15, message='Password must be 2-15 characters')])
  
    class Meta:
        csrf = False

class AgencyUpdateForm(FlaskForm):
    #passwordOld = StringField("Username",[validators.Length(min=2,max=15, message='Agencys username must be 2-15 characters')])
    password = PasswordField("Password",[validators.Length(min=2,max=15, message='Password must be 2-15 characters')])
  
    class Meta:
        csrf = False