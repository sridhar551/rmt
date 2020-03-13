import datetime
from marshmallow import fields, Schema
from . import db


class Employee(db.Model):
    __tablename = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    designation = db.Column(db.String())
    phone_number = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)


    def __init__(self, firstname=None, lastname=None, designation=None, phone_number=None, created_at=None, modified_at=None):
        self.firstname = firstname
        self.lastname = lastname
        self.designation = designation
        self.phone_number = phone_number
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

class EmployeeSchema(Schema):
  id = fields.Int(dump_only=True)
  firstname = fields.Str(required=True)
  lastname = fields.Str(required=True)
  phone_number = fields.Str(required=True)
  designation = fields.Str(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
