from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained TabNet model, scaler, and label encoder
tabnet_model = joblib.load("tabnet_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Feature names (must match training order)
feature_names = [
    "Protocol",
    "Flow IAT Mean",
    "FIN Flag Count",
    "RST Flag Count",
    "Down/Up Ratio",
    "Fwd Seg Size Min",
    "Idle Max",
    "Connection Type",
]


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probabilities = None

    if request.method == "POST":
        try:
            # Get form data and convert to float
            input_data = [float(request.form[feature]) for feature in feature_names]
            input_array = np.array([input_data])

            # Standardize input using the saved scaler
            input_scaled = scaler.transform(input_array)

            # Make prediction
            predicted_label = tabnet_model.predict(input_scaled)[0]
            predicted_probs = tabnet_model.predict_proba(input_scaled)[0]
            decoded_label = label_encoder.inverse_transform([predicted_label])[0]

            # Format probabilities
            probabilities = {
                label_encoder.inverse_transform([i])[0]: round(prob, 4)
                for i, prob in enumerate(predicted_probs)
            }

            prediction = decoded_label
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template(
        "index.html",
        feature_names=feature_names,
        prediction=prediction,
        probabilities=probabilities,
    )


if __name__ == "__main__":
    app.run(debug=True)