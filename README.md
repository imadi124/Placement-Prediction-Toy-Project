# Placement-Prediction-Toy-Project
A simple Flask web application that predicts whether a student will get placed or not based on their IQ and CGPA.
The machine learning model was trained separately and saved using `pickle` as `model.pkl`.

---

## 📂 Project Structure
```
Placement-Prediction-Toy-Project
├──modified_placement_data
├──placement_data
├──Placement_ToyProject(Jupyter notebook)
└──Placement_pred_Website/
   ├── app.py # Flask application (backend logic)
   ├── model.pkl # Trained machine learning model
   └── templates/
   └── index.html # Frontend HTML file
```


---

## 🚀 How It Works
1. **User Input**: The website takes two inputs from the user:
   - IQ
   - CGPA

2. **Prediction**: The trained model (`model.pkl`) predicts whether placement will happen or not.

3. **Output**:
   - If the model predicts `1`: `"placement ho jayega☺️"`
   - If the model predicts `0`: `"☹️placement nahi ho payega"`
<img width="1513" height="809" alt="Screenshot 2025-08-13 134906" src="https://github.com/user-attachments/assets/c10fad0c-dbb3-49da-88ec-a8bfb1a233d3" />

---

## 🛠️ Technologies Used
- Python 🐍
- Flask 🌐
- HTML5
- Pickle (for saving/loading ML model)

---

## 📦 Installation & Setup

1. **Clone this repository**  
   ```bash
   git clone https://github.com/yourusername/Placement_pred_Website.git
   cd Placement_pred_Website

2. **Install dependencies**
```
   pip install flask
```

3. **Run the Flask app**
```
python app.py
```
4. **Open in browser**
```
Go to: http://127.0.0.1:5000/
```
   
