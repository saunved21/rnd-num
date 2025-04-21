from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def random_number():
    number = random.randint(1, 100)
    return f"🎲 Your random number is: {number}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
