from myPackage.models import Student, Subject
from myPackage.models import db

def create_subjects_for_student(name, subject_names):
    # Check if student already exists
    student = Student.query.filter_by(name=name).first()
    if not student:
        # Create new student
        student = Student(name=name)
        db.session.add(student)
        db.session.commit()

    # Create subjects for student
    for subject_name in subject_names:
        subject = Subject.query.filter_by(name=subject_name).first()
        if not subject:
            subject = Subject(name=subject_name)
            db.session.add(subject)
            db.session.commit()
        student.subjects.append(subject)
    db.session.commit()

create_subjects_for_student('John', ['Math', 'Science', 'History'])
student = Student.query.filter_by(name='John').first()
for subject in student.subjects:
    print(subject.name)
