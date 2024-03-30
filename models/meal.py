from database import db
from flask_login import UserMixin

class Meal(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(120), nullable=False)
  date_and_time = db.Column(db.DateTime)
  diet = db.Column(db.Boolean, default=True)

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "date_and_time": self.date_and_time,
      "diet": self.diet
    }