from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
import datetime
from . import  db
# db = SQLAlchemy()


class Users(db.Model):
    __tablename = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, name=None, email=None, password=None, created_at=None, modified_at=None):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  email = fields.Email(required=True)
  password = fields.Str(required=True, load_only=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
  # blogposts = fields.Nested(BlogpostSchema, many=True)