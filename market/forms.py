from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from market.models import User
from flask_login import login_user, logout_user, login_required, current_user


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
    username = StringField(label="username", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="email@gmail.com", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="password", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
    
    username = StringField(label="username", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase')

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell")