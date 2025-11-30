from flask import Flask, render_template
import random

app = Flask(__name__)

CHALLENGES = [
    "Play Aimlabs for 30 minutes",
    "Play 10 deathmatches with vandal",
    "Play 10 deathmatches with phantom",
    "Play 10 deathmatches with sheriff",
    "Play 10 deathmatches with ghost",
    "Kill 25 hard bots in the range",
    "Kill 100 bots in less than 100 seconds",
    "Play 10 Teamdeathmatch",
    "Play 5 competitive mode",
    "Plant the spike 10 times",
    "Defuse the spike 10 times",
    "Kill 5 enemy with operator"
]

@app.route("/")
def index():
    challenge = random.choice(CHALLENGES)
    return render_template("index.html", challenge=challenge)

if __name__ == "__main__":
    app.run(debug=True)
