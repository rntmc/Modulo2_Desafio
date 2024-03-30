from flask import Flask, request, jsonify
from models.meal import Meal
from datetime import datetime
from database import db
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route("/add", methods=["POST"])
def create_meal():
  data = request.json
  name = data.get("name")
  description = data.get("description")
  date_and_time_str = data.get("date_and_time")

  if name and description and date_and_time_str:
    try:
      # Convert the provided date_and_time string to a datetime object
      date_and_time = datetime.strptime(date_and_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
      return jsonify({"message": "Invalid date_and_time format. Please provide date_and_time in format 'YYYY-MM-DD HH:MM:SS'"}), 400
    
    meal = Meal(name=name, description=description, date_and_time=date_and_time, diet=True) 
    db.session.add(meal)
    db.session.commit()
    return jsonify({"message": "Meal successfully added"})
  
  return ({"message": "Please provide the correct information"}), 400

@app.route("/list-meals", methods=["GET"])
def list_meals():
  meals = Meal.query.all()
  if meals:
    meals_json = [meal.to_dict() for meal in meals] # iterar sobre todos os objetos nessa lista
    return jsonify(meals_json)
  
  return jsonify({"message": "There's a problem listing your meals"}), 400

@app.route("/list-meal/<int:meal_id>", methods=["GET"])
def list_a_meal(meal_id):
  meal = Meal.query.get(meal_id)

  if meal:
    return meal.to_dict()
  
  return jsonify({"message": f"No meal is registered under the id {meal_id}"}), 404

@app.route("/delete-meal/<int:meal_id>", methods=["DELETE"])
def delete_meal(meal_id):
  meal = Meal.query.get(meal_id)

  if meal:
    db.session.delete(meal)
    db.session.commit()
    return jsonify({"message": f"The meal {meal_id} has been deleted"})
  
  return jsonify({"message": f"No meal under the id {meal_id} can be found"})

@app.route("/update-meal/<int:meal_id>", methods=["PUT"])
def update_meal(meal_id):
  meal = Meal.query.get(meal_id)

  if not meal:
    return jsonify({"message": "Meal not found"})
    
  data = request.json
  name = data.get("name")
  description = data.get("description")
  date_and_time = data.get("date_and_time")
  diet = data.get("diet")

  if name is None or description is None or diet is None :
    return jsonify({"message": "Please provide the correct information"}), 400
  
  #update fields
  meal.name = name
  meal.description = description
  meal.diet = diet

  if date_and_time:
    try:
      meal.date_and_time = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
      return jsonify({"message": "Invalid date_and_time format. Please provide date_and_time in format 'YYYY-MM-DD HH:MM:SS'"}), 400

  db.session.commit()
  return jsonify({"message": f"Meal {meal_id} successfully updated"})

if __name__ == "__main__":
  app.run(debug=True)