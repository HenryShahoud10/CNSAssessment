from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# SQLite DB setup
if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(debug=True)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

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
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    # Redirect to the game page, passing the user's name
    return redirect(f'/game?name={name}')

# Game page route
@app.route('/game')
def game():
    # Get the user's name from the URL parameters
    player_name = request.args.get('name', 'Player')
    return render_template('game.html', player_name=player_name)  # Pass the player's name to the game template

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(debug=True)
