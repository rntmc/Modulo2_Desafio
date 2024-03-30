from database import db
from flask_login import UserMixin
from datetime import datetime


class Meal(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(120), nullable=False)
  date_and_time = db.Column(db.DateTime)
  diet = db.Column(db.Boolean, default=True)