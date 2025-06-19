# app.py

from flask import Flask, request, render_template, jsonify
from scholarship_predictor import predict_eligibility

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    gpa = float(data["gpa"])
    income = int(data["income"])
    extracurriculars = int(data["extracurriculars"])
    hours = int(data["hours"])
    score = int(data["score"])

    result = predict_eligibility(gpa, income, extracurriculars, hours, score)
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
