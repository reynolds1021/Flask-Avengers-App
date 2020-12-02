from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email 


#class UserInfoForm(FlaskForm):
 #   username = StringField('Username', validators = [DataRequired()])
  #  email = StringField('Email',validators = [DataRequired(),Email()])
   # password = PasswordField('Password', validators = [DataRequired()])
    #confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    #submit = SubmitField()

class PhoneForm(FlaskForm):
    firstname = StringField('First Name', validators = [DataRequired()])
    lastname = StringField('Last Name', validators = [DataRequired()])
    heroname = StringField('Hero Name', validators = [DataRequired()])
    address = StringField('Address', validators = [DataRequired()])
    phonenumber = StringField('Phone Number', validators = [DataRequired()])
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()    

    

class LoginForm(FlaskForm):
    heroname = StringField('Heroname',validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()    


