from myPackage import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_student(student_id):
    return Student.query.get(int(student_id))


class Student(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    subjects = db.relationship('Subject', backref='students', lazy=True)


    def __repr__(self):
        return f"User('{self.name}' , '{self.email}')"

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    teacher = db.Column(db.String(50), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)


    def __repr__(self):
        return f"User('{self.name}' , '{self.teacher})"



