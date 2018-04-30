from flask import Flask
import random

app = Flask(__name__)

greetings = ['hello', 'hi', 'good morning']
places = ['region','continent', 'world']

@app.route("/hello")
def hello():
    greeting = random.choice(greetings) + " " + random.choice(places)
    return greeting

if __name__ == '__main__':
    app.run()
