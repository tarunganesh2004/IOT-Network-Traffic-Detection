from flask import Flask, request, jsonify
import numpy as np
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# Load ML components
tabnet_model = joblib.load("model/tabnet_model.pkl")
scaler = joblib.load("model/scaler.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    feature_order = [
        "Protocol",
        "Flow_IAT_Mean",
        "FIN_Flag_Count",
        "RST_Flag_Count",
        "Down_Up_Ratio",
        "Fwd_Seg_Size_Min",
        "Idle_Max",
        "Connection_Type",
    ]

    # Convert input to array
    input_values = [float(data[feature]) for feature in feature_order] # type: ignore
    input_array = np.array([input_values]).reshape(1, -1)

    # Standardize input
    input_scaled = scaler.transform(input_array)

    # Predict
    pred_label = tabnet_model.predict(input_scaled)[0]
    pred_probs = tabnet_model.predict_proba(input_scaled)[0]

    # Convert to readable format
    decoded_label = label_encoder.inverse_transform([pred_label])[0]
    class_probabilities = {
        label_encoder.inverse_transform([i])[0]: float(prob)
        for i, prob in enumerate(pred_probs)
    }

    return jsonify({"class": decoded_label, "probabilities": class_probabilities})


if __name__ == "__main__":
    app.run(debug=True)