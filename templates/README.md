# AI Academic Advisor System

## 1. Introduction

The AI Academic Advisor System is a web-based application developed using
Python, Flask, and Machine Learning.

The system uses students' academic information to recommend a computing
field they may wish to explore.

This project demonstrates the application of Artificial Intelligence
techniques and standard software engineering practices.

## 2. Objectives

- Develop a basic AI-powered academic recommendation system.
- Apply machine learning to a student dataset.
- Build a web interface for collecting student information.
- Provide recommendations based on a trained model.
- Demonstrate software development, testing, and version control.

## 3. Technologies Used

- Python
- Google Colab
- Pandas
- Scikit-learn
- Flask
- HTML
- CSS
- Git
- GitHub
- Visual Studio Code

## 4. Project Structure

```text
AI-Academic-Advisor/
├── app.py
├── train_model.ipynb
├── academic_advisor_model.pkl
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## 5. How the System Works

1. The student opens the web application.
2. The student enters their CGPA, programming skill, mathematics skill,
   and daily study hours.
3. The application validates the submitted information.
4. The trained Decision Tree model predicts a computing field.
5. The application displays the recommended field and related advice.

## 6. Machine Learning Method

A Decision Tree Classifier from Scikit-learn is used for this project.

The input features are:
- CGPA
- Programming skill
- Mathematics skill
- Daily study hours

The target variable is the recommended computing field.

The model is trained in Google Colab and saved as a Pickle file
for use in the Flask application.

## 7. Installation and Setup

Install Python and Git, then open the project folder in a terminal.

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

Run the web application:

```bash
python app.py
```

Open the following address in a browser:

http://127.0.0.1:5000

## 8. Testing

The application can be tested by entering different valid values for
CGPA, programming skill, mathematics skill, and study hours.

Confirm that the application displays a predicted field and appropriate
advice. Invalid inputs should be rejected.

## 9. Limitations

The model uses a small, synthetic dataset created for demonstration.
Its recommendations have not been validated for real academic advising.

A larger, representative dataset and evaluation with academic experts
would be needed before real-world use.

## 10. Conclusion

The AI Academic Advisor demonstrates how machine learning can be
integrated into a web application to provide basic academic field
recommendations.

The project combines AI techniques with software engineering tools
and practices.