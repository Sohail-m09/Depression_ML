import streamlit as st
from api_client import predict_depression

st.set_page_config(
    page_title="Mental Health Assessment",
    layout="wide"
)

# ==========================================================
# SECTION-WISE QUESTIONS
# ==========================================================

sections = [

    # ======================================================
    # SECTION 1 : BASIC INFORMATION
    # ======================================================

    {
        "title": "Basic Information",
        "description": "Please provide your demographic information.",

        "questions": [

            {
                "key": "age",
                "question": "What is your age?",
                "type": "number",
                "min": 15,
                "max": 80,
                "default": 25
            },

            {
                "key": "gender",
                "question": "Select your Gender",
                "type": "select",
                "options": [
                    "Male",
                    "Female",
                    "Other"
                ]
            },

            {
                "key": "marital_status",
                "question": "Marital Status",
                "type": "select",
                "options": [
                    "Single",
                    "Married",
                    "Divorced"
                ]
            },

            {
                "key": "education_level",
                "question": "Highest Education",
                "type": "select",
                "options": [
                    "High School",
                    "Bachelor",
                    "Master",
                    "PhD"
                ]
            }

        ]
    },

    # ======================================================
    # SECTION 2 : LIFESTYLE
    # ======================================================

    {
        "title": "Lifestyle",
        "description": "Tell us about your daily habits.",

        "questions": [

            {
                "key": "sleep_hours",
                "question": "How many hours do you usually sleep each night?",
                "type": "slider",
                "min": 0,
                "max": 12,
                "default": 7,
                "help":"Recommended: 7–9 hours"
            },

            {
                "key": "physical_activity_hours_per_week",
                "question": "How many hours do you exercise in a week?",
                "type": "slider",
                "min": 0,
                "max": 20,
                "default": 5,
                "help":"Recommended: At least 150 minutes/week"
            },

            {
                "key": "screen_time_hours_per_day",
                "question": "Average recreational screen time per day",
                "type": "slider",
                "min": 0,
                "max": 15,
                "default": 6,
                "help":"Lower screen time is generally healthier."
            },

            {
                "key": "social_support_score",
                "question": "How supported do you feel by your family or friends?",
                "type": "slider",
                "min": 0,
                "max": 10,
                "default": 5,
                "help":"0 = No Support | 10 = Excellent Support"
            }

        ]
    },

    # ======================================================
    # SECTION 3 : WORK & ACADEMIC
    # ======================================================

    {
        "title": "Work & Academic",
        "description": "Tell us about your work or academic life.",

        "questions": [

            {
                "key": "employment_status",
                "question": "Employment Status",
                "type": "select",
                "options": [
                    "Employed",
                    "Student",
                    "Unemployed",
                    "Self-Employed"
                ]
            },

            {
                "key": "working_hours_per_week",
                "question": "Working Hours Per Week",
                "type": "slider",
                "min": 0,
                "max": 80,
                "default": 40
            },

            {
                "key": "work_stress_level",
                "question": "How stressful is your work life?",
                "type": "slider",
                "min": 0,
                "max": 10,
                "default": 5,
                "help":"0 = No Stress | 10 = Extremely Stressful"
            },

            {
                "key": "academic_pressure_level",
                "question": "How much academic pressure do you feel?",
                "type": "slider",
                "min": 0,
                "max": 10,
                "default": 5,
                "help":"0 = None | 10 = Extremely High"
            },

            {

            "key": "job_satisfaction_score",
            "question": "How satisfied are you with your work or studies?",
            "type": "slider",
            "min": 0,
            "max": 10,
            "default": 5,
            "help": "0 = Very Dissatisfied | 10 = Very Satisfied"

            },

            {

            "key": "financial_stress_level",
            "question": "How much financial stress do you currently experience?",
            "type": "slider",
            "min": 0,
            "max": 10,
            "default": 5,
            "help": "0 = No Financial Stress | 10 = Extremely High"
            
            }

        ]
    },

    # ======================================================
    # SECTION 4 : MENTAL HEALTH
    # ======================================================

    {
        "title": "Mental Health",
        "description": "Please answer honestly.",

        "questions": [

            {
                "key": "anxiety_score",
                "question": "How anxious have you felt recently?",
                "type": "slider",
                "min": 0,
                "max": 10,
                "default": 5,
                "help":"0 = Never | 10 = Very Often"
            },

            {
                "key": "depression_score",
                "question": "How often have you felt sad or hopeless recently?",
                "type": "slider",
                "min": 0,
                "max": 10,
                "default": 5,
                "help":"0 = Never | 10 = Very Often"
            },

            {
                "key": "stress_level",
                "question": "How stressed do you usually feel?",
                "type": "slider",
                "min": 0,
                "max": 10,
                "default": 5,
                "help": "0 = Very Low | 10 = Extremely High"
            },

            {
                "key": "mood_swings_frequency",
                "question": "How often do your emotions change suddenly?",
                "type": "slider",
                "min": 0,
                "max": 10,
                "default": 5,
                "help":"0 = Never | 10 = Very Frequently"
            }

        ]
    },

    # ======================================================
    # SECTION 5 : CLINICAL HISTORY
    # ======================================================

    {
        "title": "Clinical History",
        "description": "Medical and psychological history.",

        "questions": [

            {
                "key": "concentration_difficulty_level",
                "question": "How difficult is it to concentrate on daily tasks?",
                "type": "slider",
                "min": 0,
                "max": 10,
                "default": 5,
                "help":"0 = Very Easy | 10 = Extremely Difficult"
            },

            {
                "key": "panic_attack_history",
                "question": "Have you ever experienced a panic attack?",
                "type": "select",
                "type": "radio"
            },

            {
                "key": "family_history_mental_illness",
                "question": "Does anyone in your family have a history of mental illness?",
                "type": "select",
                "type": "radio"
            },

            {
                "key": "previous_mental_health_diagnosis",
                "question": "Previous Mental Health Diagnosis",
                "type": "select",
                "type": "radio"
            }

        ]
    },

    # ======================================================
    # SECTION 6 : ADDITIONAL INFORMATION
    # ======================================================

    {
        "title": "Additional Information",
        "description": "Final questions before prediction.",

        "questions": [

            {
                "key": "therapy_history",
                "question": "Have you ever received therapy or counseling?",
                "type": "select",
                "type": "radio" 
            },

            {
                "key": "substance_use",
                "question": "Do you currently use alcohol, tobacco, or any other substances frequently?",
                "type": "select",
                "type": "radio"
            }

        ]
    }

]

# ==========================================================
# SESSION STATE
# ==========================================================

if "current_page" not in st.session_state:
    st.session_state.current_page = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# ==========================================================
# CURRENT PAGE
# ==========================================================

page = st.session_state.current_page

TOTAL_PAGES = len(sections)

current_section = sections[page]

progress = (page + 1) / TOTAL_PAGES

# ==========================================================
# HEADER
# ==========================================================

st.progress(progress)

st.caption(f"{int(progress*100)}% Completed")

with st.container(border=True):

    st.markdown(f"## {current_section['title']}")

    st.write(current_section["description"])

    st.caption(f"Section {page + 1} of {TOTAL_PAGES}")

st.divider()

# ==========================================================
# QUESTIONS
# ==========================================================

for question in current_section["questions"]:

    with st.container(border=True):

        st.markdown(f"#### {question['question']}")

        if "help" in question:
            st.caption(question["help"])

        if question["type"] == "number":

            value = st.number_input(
                label="",
                min_value=question["min"],
                max_value=question["max"],
                value=question["default"],
                key=question["key"]
            )

        elif question["type"] == "slider":

            value = st.slider(
                label="",
                min_value=question["min"],
                max_value=question["max"],
                value=question["default"],
                key=question["key"]
            )

        elif question["type"] == "select":

            value = st.selectbox(
                label="",
                options=question["options"],
                key=question["key"]
            )

        elif question["type"] == "radio":
            option = st.radio(
                label = "",
                options = ["Yes", "No"],
                horizontal = True,
                key = question["key"]
            )

            value = 1 if option == "Yes" else 0

        st.session_state.answers[question["key"]] = value

# ==========================================================
# NAVIGATION
# ==========================================================

st.divider()

left, center, right = st.columns([1,3,1])

with left:

    if page > 0:

        if st.button("Previous", use_container_width=True):

            st.session_state.current_page -= 1
            st.rerun()

with right:

    if page < TOTAL_PAGES - 1:

        if st.button("Next", use_container_width=True):

            st.session_state.current_page += 1
            st.rerun()

    else:

       if st.button("Submit Assessment", use_container_width=True):

        with st.spinner("Analyzing your responses..."):

            st.write(st.session_state.answers)
            result = predict_depression(st.session_state.answers)

        if "error" in result:

            st.error("Unable to connect to the Prediction API.")

            st.write(result["error"])

        else:

            # Save API response
            st.session_state.result = result

            # Move to Result Page
            st.switch_page("pages/results.py")