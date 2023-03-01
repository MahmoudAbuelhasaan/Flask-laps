from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,validators,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from myPackage.models import Student


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    
    def validate_username(self,username):
        student = Student.query.filter_by(name=username.data).first()
        if student:
            raise ValidationError('Username already exists')
			

    def validate_email(self,email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Username already exists')
			


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


class SubjectForm(FlaskForm):
    name = StringField('Subject Name', validators=[DataRequired()])
    teacher = StringField('Teacher Name', validators=[DataRequired()])
    student_id = StringField('Student ID', validators=[DataRequired()])
    submit = SubmitField('Add Subject')