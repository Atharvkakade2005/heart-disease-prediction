from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load Random Forest model
model = joblib.load("model/random_forest_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get input values
    age = float(request.form["age"])
    sex = float(request.form["sex"])
    cp = float(request.form["cp"])
    trestbps = float(request.form["trestbps"])
    chol = float(request.form["chol"])
    fbs = float(request.form["fbs"])
    restecg = float(request.form["restecg"])
    thalach = float(request.form["thalach"])
    exang = float(request.form["exang"])
    oldpeak = float(request.form["oldpeak"])
    slope = float(request.form["slope"])
    ca = float(request.form["ca"])
    thal = float(request.form["thal"])

    # Create input array
    input_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    # Random Forest was trained on unscaled data
    prediction = model.predict(input_data)[0]

    # Prediction probability
    probability = model.predict_proba(input_data)[0][1]

    # Result
    if prediction == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease Detected"

    return render_template(
        "index.html",
        prediction=result,
        probability=round(probability * 100, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)