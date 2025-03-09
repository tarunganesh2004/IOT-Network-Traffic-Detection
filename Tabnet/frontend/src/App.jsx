// @ts-nocheck
import { useState } from "react";
import "./index.css";

function App() {
  const [formData, setFormData] = useState({
    Protocol: "",
    Flow_IAT_Mean: "",
    FIN_Flag_Count: "0",
    RST_Flag_Count: "",
    Down_Up_Ratio: "",
    Fwd_Seg_Size_Min: "",
    Idle_Max: "",
    Connection_Type: "0",
  });

  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    setPrediction(data);
  };

  return (
    <div className="main-container">
      <h2>IoT Network Traffic Prediction</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-grid">
          {Object.keys(formData).map((key, index) => (
            <div key={key} className="form-group">
              <label>{key.replace(/_/g, " ")}:</label>
              {key === "Connection_Type" || key === "FIN_Flag_Count" ? (
                <select
                  name={key}
                  value={formData[key]}
                  onChange={handleChange}
                  required
                  className="dropdown"
                >
                  {key === "Connection_Type" ? (
                    <>
                      <option value="0">0</option>
                      <option value="1">1</option>
                    </>
                  ) : (
                    <>
                      <option value="0">0</option>
                      <option value="1">1</option>
                      <option value="2">2</option>
                    </>
                  )}
                </select>
              ) : (
                <input
                  type="text"
                  name={key}
                  value={formData[key]}
                  onChange={handleChange}
                  required
                />
              )}
            </div>
          ))}
        </div>
        <button type="submit">Predict</button>
      </form>

      {prediction && (
        <div className="prediction-container">
          <h3>Prediction Result</h3>
          <p>
            <strong>Predicted Class:</strong> {prediction.class}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
