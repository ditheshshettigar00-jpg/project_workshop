from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("frontend.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    district = data.get("district")
    income = float(data.get("income", 0))
    households = float(data.get("households", 0))
    nightlight = float(data.get("nightlight", 0))

    # Simple sample calculation
    # Replace this section with your trained ML model later
    if nightlight < 20:
        score = 0.75
        status = "High Deprivation"

    elif nightlight < 50:
        score = 0.52
        status = "Moderate Deprivation"

    else:
        score = 0.25
        status = "Low Deprivation"

    result = {
        "district": district,
        "deprivation_score": score,
        "status": status
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)