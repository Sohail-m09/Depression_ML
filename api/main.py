from fastapi import FastAPI
from api.schema import DepressionInput
import joblib
import pandas as pd
import shap

app = FastAPI()
model = joblib.load("models/best_xgboost_pipeline.pkl")
feature_names = joblib.load("models/fiture_names.pkl")
label_mapping = joblib.load("models/risk_mapping.pkl")

classifier = model.named_steps["classifier"]

background = model.named_steps["preprocessor"].transform(
    pd.DataFrame([{
        "age": 25,
        "gender": "Male",
        "marital_status": "Single",
        "education_level": "Bachelor",
        "employment_status": "Employed",
        "sleep_hours": 7,
        "physical_activity_hours_per_week": 3,
        "screen_time_hours_per_day": 4,
        "social_support_score": 5,
        "work_stress_level": 5,
        "academic_pressure_level": 5,
        "job_satisfaction_score": 5,
        "financial_stress_level": 5,
        "working_hours_per_week": 40,
        "anxiety_score": 5,
        "depression_score": 5,
        "stress_level": 5,
        "mood_swings_frequency": 5,
        "concentration_difficulty_level": 5,
        "panic_attack_history": 0,
        "family_history_mental_illness": 0,
        "previous_mental_health_diagnosis": 0,
        "therapy_history": 0,
        "substance_use": 0
    }])
)

explainer = shap.Explainer(
    classifier.predict,
    background
)

@app.get("/")
def home():
    return {
        "message" : "Depression Prediction API is Running"
    }

@app.post("/predict")
def predict(data: DepressionInput):

    # Convert Pydantic model to dictionary
    input_data = data.model_dump()

    # Convert dictionary to DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict using the trained pipeline 
    prediction = model.predict(input_df)

    # Finding the probability 
    probability = model.predict_proba(input_df)

    predicted_class = int(prediction[0])

    # Convert the numeric prediction to label 
    risk = label_mapping[predicted_class]

    # Showing the confidence score
    confidence = round(float(max(probability[0])) * 100 ,2)


    # SHAP Explainability
    transformed_data = model.named_steps["preprocessor"].transform(input_df)

    shap_values = explainer(transformed_data)


    try:
        class_shap = shap_values[0, :, predicted_class]
    except Exception:
        class_shap = shap_values.values[0]

    importance = list(zip(feature_names, class_shap))

    # sort by absolute SHAP values

    importance = sorted(
        importance,
        key = lambda x: abs(x[1]),
        reverse = True
    )

    ignore_words = [
        "gender",
        "marital_status",
        "education_level",
        "employment_status",
        "age"
    ]

    feature_mapping = {
        "num__anxiety_score": "Anxiety Score",
        "num__depression_score": "Depression Score",
        "num__stress_level": "Stress Level",
        "num__financial_stress_level": "Financial Stress",
        "num__social_support_score": "Social Support",
        "bin__sleep_hours": "Sleep Duration",
        "bin__physical_activity_hours_per_week": "Physical Activity",
        "bin__screen_time_hours_per_day": "Screen Time",
        "num__working_hours_per_week": "Working Hours",
        "num__work_stress_level": "Work Stress",
        "num__academic_pressure_level": "Academic Pressure",
        "num__concentration_difficulty_level": "Concentration Difficulty",
        "num__mood_swings_frequency": "Mood Swings",
        "num__panic_attack_history": "Panic Attack History",
        "num__therapy_history": "Therapy History",
        "num__substance_use": "Substance Use"
    }

    # Top 3 important features

    top_features = []

    for feature, value in importance:
        if any(word in feature for word in ignore_words):
            continue
        display_name = feature_mapping.get(feature, feature)

        top_features.append(
            {
            "feature" : display_name,
            "impact" : round(float(value), 3)
            }
        )

        if len(top_features) == 3:
            break

        recommendation_mapping = {

        "Anxiety Score":
            "Practice relaxation techniques such as meditation and deep breathing exercises.",

        "Depression Score":
            "Consider consulting a qualified mental health professional for further assessment.",

        "Stress Level":
            "Identify major stress triggers and include relaxation breaks in your routine.",

        "Financial Stress":
            "Consider financial planning or discuss financial concerns with someone you trust.",

        "Social Support":
            "Stay connected with trusted family members or close friends.",

        "Sleep Duration":
            "Aim for 7–9 hours of quality sleep each night.",

        "Physical Activity":
            "Aim for at least 30 minutes of physical activity most days of the week.",

        "Screen Time":
            "Reduce recreational screen time, especially before bedtime.",

        "Working Hours":
            "Maintain a healthy work-life balance and avoid prolonged working hours.",

        "Work Stress":
            "Take regular breaks and maintain a healthy work-life balance.",

        "Academic Pressure":
            "Create a realistic study schedule and avoid excessive workload.",

        "Concentration Difficulty":
            "Practice mindfulness and avoid multitasking whenever possible.",

        "Mood Swings":
            "Track emotional changes and seek support if symptoms become frequent.",

        "Panic Attack History":
            "If panic attacks continue, consult a mental health professional.",

        "Therapy History":
            "Continue following the guidance provided by your mental health professional.",

        "Substance Use":
            "Consider reducing substance use and seek professional support if required."
    }

    recommendations = []
    for item in top_features:
        recommendation = recommendation_mapping.get(item["feature"])

        if recommendation:
            recommendations.append(recommendation)

        if risk == "High Risk":

            summary = (
                "The AI model predicts a High Risk level. "
                "The features below contributed the most to this prediction."
            )

        elif risk == "Moderate Risk":

            summary = (
                "The AI model predicts a Moderate Risk level. "
                "The following factors had the highest influence on the prediction."
            )

        else:

            summary = (
                "The AI model predicts a Low Risk level. "
                "The following features contributed the most to the prediction."
            )
    return {
        "prediction" : risk,
        "confidence" : f"{confidence}%",
        "summary" : summary,
        "top_contributing_features" : top_features,
        "recommendations" : recommendations
    }