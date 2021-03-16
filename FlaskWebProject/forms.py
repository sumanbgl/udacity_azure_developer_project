
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class IncomeExpenseForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    date = DateField('Date', format='%m/%d/%y',
                          render_kw={'placeholder': '3/16/21 for March 16, 2021'}, validators=[DataRequired()])
    submit = SubmitField('Save')    