from flask_wtf import FlaskForm
from wtforms import StringField,FileField,DateField,SubmitField,IntegerField,RadioField,SelectField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length,equal_to
class RegistrationForm(FlaskForm):
    username = StringField("username",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired(),Length(min=8,max=20)])
    repeat_password = PasswordField("repeat password",validators=[DataRequired(),equal_to("password")])
    phone_number = IntegerField("phone number",validators=[DataRequired()])
    gender = RadioField("select gender",choices=["male","female"],validators=[DataRequired()])
    birthday = DateField("birth date",validators=[DataRequired()])

    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    img = FileField()
    name = StringField("product name")
    price = IntegerField("price")

    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField()
    password = PasswordField()

    login = SubmitField('login')