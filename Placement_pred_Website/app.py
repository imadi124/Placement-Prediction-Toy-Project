from flask import Flask, render_template, request
import pickle

# Load the saved model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    iq = float(request.form['iq'])
    cgpa = float(request.form['cgpa'])

    # Make prediction
    prediction = model.predict([[iq, cgpa]])[0]

    if prediction == 1:
        result = "Placement ho jayega☺️"
    else:
        result = "Placement nahi ho payega☹️"

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
