import os
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use the DATABASE_URL environment variable for the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://ud5q391b26i1g7:paf97f238d4826832beda56832595b507f4be3b6be6efc687ad01fbad14c8fab1@c3gtj1dt5vh48j.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d5eikquvd8rjo7')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Registration page route
@app.route('/')
def registration_page():
    return render_template('register.html')

# Handle registration form submission
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    # Save the registered user's info into the database
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    # Redirect to the game page, passing the user's name
    return redirect(f'/game?name={name}')

# Game page route
@app.route('/game')
def game():
    # Get the user's name from the URL parameters
    player_name = request.args.get('name', 'Player')
    return render_template('game.html', player_name=player_name)

if __name__ == '__main__':
    app.run(debug=True)
