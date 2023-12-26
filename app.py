from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)
templates = [
    {
        "inputs": 6,
        "category": "sports",
        "word": "tennis"
    },
    {
        "inputs": "10",
        "category": "sports",
        "word": "basketball"
    },
    {
        "inputs": "5",
        "category": "musical instrument",
        "word": "piano"
    },
    {
        "inputs": "6",
        "category": "musical instrument",
        "word": "guitar"
    }
]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
    })

if __name__ == '__main__':
  app.run()