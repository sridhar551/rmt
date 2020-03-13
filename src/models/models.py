from flask_sqlalchemy import SQLAlchemy
import datetime
from . import  db
# db = SQLAlchemy()


class Employee( db.Model):
    __tablename = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    designation = db.Column(db.String())
    phone_number = db.Column(db.Integer)

    def __init__(self, firstname=None, lastname=None, designation=None, phone_number=None):
        self.firstname = firstname
        self.lastname = lastname
        self.designation = designation
        self.phone_number = phone_number


class Project(db.Model):
    __tablename = 'project'

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String())
    manager_name = db.Column(db.String())
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    description = db.Column(db.String())

    def __init__(self, project_name=None, manager_name=None, start_date=None, end_date=None, description=None):
        self.project_name = project_name
        self.manager_name = manager_name
        self.start_date = start_date
        self.description = description


class Skills(db.Model):
    __tablename = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init(self, name=None):
        self.name = name


class EmployeeSkill(db.Model):
    __tablename = 'employee_skill'

    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer,  db.ForeignKey('skills.id'))
    emp_id = db.Column(db.Integer,  db.ForeignKey('employee.id'))
    rating = db.Column(db.Integer)
    is_certified = db.Column(db.Boolean)

    def __init__(self, skill_id=None, emp_id=None, rating=None, is_certified=None):
        self.skill_id = skill_id
        self.emp_id = emp_id
        self.rating = rating
        self.is_certified = is_certified


class ProjectEmployee(db.Model):
    __tablename = 'project_employee'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer,  db.ForeignKey('project.id'))
    emp_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

    def __init__(self, project_id=None, emp_id=None):
        self.project_id = project_id
        self.emp_id = emp_id