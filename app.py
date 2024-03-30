from flask import Flask, request, jsonify
from models.meal import Meal
from database import db
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# @app.route("/add", methods=["POST"])
# def create_meal():
#   data = request.json()



if __name__ == "__main__":
  app.run(debug=True)