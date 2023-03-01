
from flask import render_template,request, redirect, flash, url_for
from .forms import RegistrationForm , LoginForm,SubjectForm
from myPackage import app,db
from .models import Student, Subject
from flask_bcrypt import Bcrypt
from flask_login import login_user ,current_user,logout_user,login_required


bcrypt = Bcrypt()



navigation_items = [
    {"title": "Home", "view_function": "home"},
    {"title": "About", "view_function": "about"},
]
@app.route("/nav")
def nav():
    
    return render_template("layout.html", navigation_items=navigation_items)

@app.route("/")
def home():
     return render_template("home.html", navigation_items=navigation_items)

@app.route("/about")
@login_required
def about():
     return render_template("about.html", navigation_items=navigation_items)



@app.route("/register", methods=["GET", "POST"])
def register():
    registrationForm = RegistrationForm()
    if request.method == 'POST':
        # get form data
        name = request.form.get('name')
        email = request.form.get('email')
        
        password = bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8')

        # create a new student object and add it to the database
        with app.app_context():
            student = Student(name=name, email=email, password=password)
            db.session.add(student)
            db.session.commit()

        # display success message and redirect to home page
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    # if the request method is GET, display the registration form
    return render_template('register.html')


   



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        student = Student.query.filter_by(name=username).first()
        if student and bcrypt.check_password_hash(student.password,password):
             login_user(student)
             flash('Login successful!', 'success')
             return redirect(url_for('home'))
            
        else:
            flash('Invalid name or password', 'danger')
            return redirect(url_for('login'))

   
       
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/create_db')
def create_db():
    db.create_all()
    return 'Database created successfully!'


@app.route('/subjects', methods=['GET', 'POST'])
def add_subject():
    form = SubjectForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            name = form.name.data
            student_id = form.student_id.data
            teacher = form.teacher.data

            student = Student.query.get(student_id)
            if not student:
                flash(f"No student with id {student_id} found", 'danger')
                return redirect(url_for('add_subject'))


            subject = Subject(name=name, student_id=student_id, teacher=teacher)
            db.session.add(subject)
            db.session.commit()
            flash('Subject added successfully!', 'success')
            return redirect(url_for('home'))

    return render_template('add_subject.html', form=form)



