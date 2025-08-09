from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open('data/exercises.json') as f:
    exercises = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    program = []
    if request.method == "POST":
        program_type = request.form.get("program_type")
        if program_type in exercises:
            program = exercises[program_type]
    return render_template("index.html", program=program)

if __name__ == "__main__":
    app.run(debug=True)
