from flask import Flask, render_template, request, redirect, url_for, session
import random
import json

FILES = "users.json"

def load_users():
    with open(FILES, "r") as f:
        return json.load(f)

def save_users(users):
    with open(FILES, "w") as f:
        json.dump(users, f, indent=4)

users = load_users()

app = Flask(__name__)
app.secret_key = "your-secret-key"

CHALLENGES = [
    "Play Aimlabs for 30 minutes",
    "Play 10 deathmatches with a vandal",
    "Play 10 deathmatches with a phantom",
    "Play 10 deathmatches with a sheriff",
    "Play 10 deathmatches with a ghost",
    "Kill 25 hard bots in the range",
    "Kill 100 bots in less than 100 seconds",
    "Play 10 Teamdeathmatch",
    "Play 5 competitive mode",
    "Plant the spike 10 times",
    "Defuse the spike 10 times",
    "Kill 15 hard bots in the range",
    "Kill 20 hard bots in the range using jett knives",
    "Master 1 agent in each role",
    "Win 3 competitive match while leading your team",
    "Kill 5 enemy with an operator"
]

@app.route("/home")
def index():
    if session.get('username') is not None:
        username = session.get('username')
        challenge = random.choice(CHALLENGES)
        return render_template("index.html", challenge=challenge, users=users, username=username)
    else:
        return redirect(url_for('login'))

@app.route("/", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        loginSuccess = any(user["username"] == username for user in users)

        if loginSuccess:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template("login.html")

    return render_template("login.html")

@app.route("/add-score")
def addScore():
    username = session.get('username')
    for user in users:
        if user["username"] == username:
            user["score"] = int(user["score"]) + 1
            save_users(users)
    return redirect(url_for('index'))

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
