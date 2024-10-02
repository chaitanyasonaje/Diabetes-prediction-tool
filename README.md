

---

# Diabetes Detection Website

## Overview

The **Diabetes Detection Website** is a machine learning-based web application that predicts the likelihood of diabetes based on user input. This model uses patient data such as glucose level, blood pressure, BMI, and other medical information to provide a probability of diabetes occurrence. The web application features an advanced UI with animations for a seamless user experience.

### Features:
- **Diabetes Prediction:** Predict the likelihood of having diabetes based on health parameters.
- **Modern UI Design:** A clean and responsive interface with animations for an enhanced user experience.
- **Interactive Form:** User-friendly input fields to enter relevant medical data.
- **Instant Results:** Immediate predictions based on the user's input data.
- **Mobile-Friendly:** Fully responsive for use on mobile devices.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Model Description](#model-description)
5. [Technology Stack](#technology-stack)
6. [Features](#features)
7. [Contributing](#contributing)
8. [License](#license)

---

## Installation

### Prerequisites:
- Python 3.x
- Flask
- scikit-learn
- Pandas
- HTML, CSS for the frontend

### Steps to Set Up Locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/chaitanyasonaje/diabetes-detection-website.git
   ```
   
2. **Navigate to the Project Directory**:
   ```bash
   cd diabetes-detection-website
   ```

3. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Open the Application in a Browser**:
   Navigate to `http://127.0.0.1:5000/` to access the web app.

---

## Usage

Once the application is running:

1. Fill out the form with the required medical details:
   - Pregnancies
   - Glucose
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - BMI
   - Diabetes Pedigree Function
   - Age
2. Click on the **Predict** button.
3. The result will display the likelihood of having diabetes.

---

## Project Structure

```bash
diabetes-detection-website/
│
├── static/
│   └── style.css          # CSS for styling and animations
│
├── templates/
│   └── index.html         # HTML for the frontend
│
├── app.py                 # Main application file (Flask server)
├── model.pkl              # Pre-trained machine learning model
├── README.md              # This README file
├── requirements.txt       # List of dependencies
└── .gitignore             # Git ignore file
```

---

## Model Description

The model used for prediction is based on a **Logistic Regression** algorithm trained on the famous **PIMA Indians Diabetes Dataset**. The dataset contains medical data for 768 patients, with features like:

- **Pregnancies**: Number of pregnancies
- **Glucose**: Plasma glucose concentration
- **Blood Pressure**: Diastolic blood pressure
- **Skin Thickness**: Triceps skinfold thickness
- **Insulin**: 2-hour serum insulin
- **BMI**: Body mass index
- **Diabetes Pedigree Function**: Diabetes pedigree function score
- **Age**: Age in years

The model achieves an accuracy of approximately 75% on the testing set. It predicts whether a person is at risk of having diabetes based on these health parameters.

---

## Technology Stack

- **Backend**: Flask (Python-based micro web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Model**: Logistic Regression
- **Deployment**: Flask application running locally or on a server.

---

## Features

1. **Machine Learning-Powered Prediction**: Uses a trained model to predict the likelihood of diabetes.
2. **User-Friendly UI**: A modern and clean design that is easy to navigate and mobile-friendly.
3. **Fast Results**: Real-time predictions based on user input data.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any queries or suggestions, feel free to contact:

- **Name**: Chaitanya Sonaje
- **GitHub**: [chaitanyasonaje](https://github.com/chaitanyasonaje)
- **Email**: [chaitanyasonaje0205@gmail.com](mailto:chaitanyasonaje0205@gmail.com)

---

