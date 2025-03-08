// @ts-nocheck
import { useState } from 'react';
import './index.css';

function App() {
  const [formData, setFormData] = useState({
    Protocol: '',
    Flow_IAT_Mean: '',
    FIN_Flag_Count: '',
    RST_Flag_Count: '',
    Down_Up_Ratio: '',
    Fwd_Seg_Size_Min: '',
    Idle_Max: '',
    Connection_Type: ''
  });
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });
    const data = await response.json();
    setPrediction(data);
  };

  return (
    <div className="container">
      <div className="form-container">
        <h2>IoT Traffic Prediction</h2>
        <form onSubmit={handleSubmit}>
          {Object.keys(formData).map((key) => (
            <div key={key}>
              <label>{key.replace(/_/g, ' ')}:</label>
              <input type="text" name={key} value={formData[key]} onChange={handleChange} required />
            </div>
          ))}
          <button type="submit">Predict</button>
        </form>
      </div>
      {prediction && (
        <div className="result-container">
          <h3>Prediction Result</h3>
          <p><strong>Predicted Class:</strong> {prediction.class}</p>
          {/* <h4>Class Probabilities:</h4>
          <ul>
            {Object.entries(prediction.probabilities).map(([label, prob]) => (
              <li key={label}>{label}: {prob.toFixed(4)}</li>
            ))}
          </ul> */}
        </div>
      )}
    </div>
  );
}

export default App;