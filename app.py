from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load the trained machine learning model
MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "academic_advisor_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# Academic advice for each recommended field
advice = {
    "AI and Machine Learning":
        "Explore Artificial Intelligence, Machine Learning, "
        "Python programming, and mathematics.",

    "Software Engineering":
        "Focus on programming, software design, web development, "
        "testing, and building practical projects.",

    "Data Science":
        "Develop skills in statistics, Python, databases, "
        "data analysis, and data visualization.",

    "General Computing":
        "Strengthen your computer science fundamentals, "
        "programming skills, and problem-solving abilities."
}


@app.route("/", methods=["GET", "POST"])
def home():
    recommendation = None
    message = None

    if request.method == "POST":
        try:
            cgpa = float(request.form["cgpa"])
            programming = int(request.form["programming"])
            mathematics = int(request.form["mathematics"])
            study_hours = float(request.form["study_hours"])

            # Validate the submitted information
            if not 0 <= cgpa <= 5:
                raise ValueError("CGPA must be between 0 and 5.")

            if not 1 <= programming <= 5:
                raise ValueError(
                    "Programming skill must be between 1 and 5."
                )

            if not 1 <= mathematics <= 5:
                raise ValueError(
                    "Mathematics skill must be between 1 and 5."
                )

            if not 0 <= study_hours <= 24:
                raise ValueError(
                    "Study hours must be between 0 and 24."
                )

            # Ask the AI model to make a prediction
            prediction = model.predict([[
                cgpa,
                programming,
                mathematics,
                study_hours
            ]])[0]

            recommendation = {
                "field": prediction,
                "advice": advice.get(
                    prediction,
                    "Continue developing your academic skills."
                )
            }

        except ValueError as error:
            message = str(error)

        except Exception:
            message = (
                "Something went wrong. Check your entries "
                "and try again."
            )

    return render_template(
        "index.html",
        recommendation=recommendation,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)