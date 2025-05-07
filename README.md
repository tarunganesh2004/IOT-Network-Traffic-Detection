# 🌐 IoT Network Traffic Detection using TabNet 

## 📌 Project Overview
This project focuses on detecting and classifying IoT network traffic using deep learning models. The goal is to predict the type of network traffic based on extracted features from the **ACI IoT 2023 dataset**. Multiple models were evaluated, and **TabNet** was chosen as the final model for deployment. A **React-based web application** was developed for real-time predictions. 

---

## 📂 Dataset
📊 **ACI IoT 2023 Dataset**: The original dataset consists of **85 columns** with network traffic features. After preprocessing, it was reduced to **8 essential features**:

🔹 `Protocol`  
🔹 `Flow IAT Mean`  
🔹 `FIN Flag Count`  
🔹 `RST Flag Count`  
🔹 `Down/Up Ratio`  
🔹 `Fwd Seg Size Min`  
🔹 `Idle Max`  
🔹 `Connection Type`  

---

## ⚙️ Features & Methodology

### 🛠 **Data Preprocessing**:
✔️ Reduced dataset from **85 to 35 and then 8 relevant features**  
✔️ Handled missing values  
✔️ Encoded categorical variables  
✔️ Normalized numerical features using **StandardScaler**  
✔️ Split dataset into **80% training** and **20% testing**  

### 🤖 **Modeling Approaches**:
🔹 **Multi Layer Perceptron** (Simple Deep learning model)  
🔹 **Autoencoder** (Anomaly Detection Approach)  
🔹 **Resnet** (with residual connections)  
🔹 **TabNet** (Final Chosen Model)  

### 📊 **Evaluation Metrics & Visualizations**:
✔️ **Accuracy Score**  
✔️ **Confusion Matrix** (heatmap)   
✔️ **Precision-Recall Curve**  
✔️ **ROC Curve with AUC Scores**  
✔️ **Feature Importance Plot** (Top 10 important features)  

---

## 🚀 Web Application (React + Flask)
A **React-based web application** is built to take user inputs for the following key features and display the **TabNet model's prediction**.

### 🔹 **How It Works**:
1️⃣ The user enters feature values in a **React web form**.  
2️⃣ The form sends the input data to a **Flask API**.  
3️⃣ The **TabNet model** processes the inputs.  
4️⃣ The **predicted network traffic type** is displayed on the React UI.  

---

## 🛠 Installation & Usage

### 🔧 **Prerequisites**
- Python 3.x  
- Flask  
- PyTorch (for TabNet)  
- Scikit-learn  
- React.js  
- Axios (for API calls)  

### 📥 **Installation**
```bash
# Clone the repository
git clone https://github.com/tarunganesh2004/IoT-Network-Traffic-Detection.git
cd IoT-Network-Traffic-Detection

# Install frontend dependencies
cd tabnet/frontend
npm install
```

### ▶️ **Run the Application**
#### Start the Backend (Flask API)
```bash
cd tabnet/backend
python app.py
```
#### Start the Frontend (React App)
```bash
cd tabnet/frontend
npm start
```
Then open **http://localhost:3000/** in your browser.  

---

## 📊 Results & Analysis
- **TabNet outperformed other models** in classifying IoT network traffic.  
- **Decision Tree** provided a simple but less accurate baseline.  
- **Autoencoder** helped in understanding anomaly detection but was not suitable for final deployment.  
- **SGDClassifier** was tested with log loss calibration but was not chosen as the final model.  
- **Visualization techniques** helped analyze network behavior and model predictions.  

---

## 🏆 Key Takeaways
✔️ Feature reduction improved model performance.  
✔️ TabNet was the most effective model for IoT traffic classification.  
✔️ React + Flask integration allowed for a smooth web-based prediction system.  

---

## 🤝 Contributors 
- **Vinayraj** - Developer & Contributer
- **Tarun Ganesh** - Developer & Researcher 

---

## 📜 License
This project is open-source under the **MIT License**.  

---

🚀 **Future Work:** Implement real-time traffic analysis and optimize models for better accuracy.  

