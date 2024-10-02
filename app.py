from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the trained model
model = joblib.load('diabetes_model.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define home route
@app.route('/')
def home():
    return render_template('index.html')

# Define prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        pregnancies = int(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes_pedigree'])
        age = int(request.form['age'])

        # Create input array for model
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])

        # Get prediction from model
        prediction = model.predict(input_data)

        # Interpret the prediction
        if prediction[0] == 1:
            result = 'The patient is likely to have diabetes.'
        else:
            result = 'The patient is unlikely to have diabetes.'

        return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
