from myPackage import db,app
import sys


def create_db():
    with app.app_context():

        db.create_all()


def create_student():
    with app.app_context():

        db.create_all()



if __name__ == '__main__':
    globals()[sys.argv[1]]()