import streamlit as st

st.set_page_config(
    page_title="AI Depression Risk Assessment",
    page_icon="🧠",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:bold;
    text-align:center;
    color:#1f4e79;
}

.sub-title{
    font-size:20px;
    text-align:center;
    color:#555555;
}

.feature-card{
    padding:20px;
    border-radius:12px;
    background:white;
    border:1px solid #d9d9d9;
    margin-bottom:18px;
    color:#111111;
}

.feature-card h4{
    color:#1f4e79;
    margin-bottom:10px;
}

.feature-card p{
    color:#333333;
    font-size:16px;
}

.disclaimer{
    background:#fff8e5;
    border-left:6px solid orange;
    padding:18px;
    border-radius:10px;
    color:#222222;
}

.disclaimer b{
    color:#d35400;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TITLE
# ==========================================================

st.markdown(
    "<div class='main-title'>AI-Based Depression Risk Assessment</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>An Explainable AI system for early mental health risk prediction.</div>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("## About this Assessment")

st.write("""
This assessment evaluates various lifestyle, psychological,
work-related and behavioural factors to estimate the likelihood
of depression risk using a Machine Learning model.

The prediction is accompanied by Explainable AI (SHAP),
allowing you to understand why the model reached its decision.
""")

st.write("")

# ==========================================================
# FEATURES
# ==========================================================

st.markdown("## What You'll Receive")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):
        st.subheader("AI Prediction")
        st.write(
            "Receive an AI-generated prediction of your depression risk level."
        )

    with st.container(border=True):
        st.subheader("Explainable AI")
        st.write(
            "Understand which factors influenced the prediction using SHAP."
        )

with col2:

    with st.container(border=True):
        st.subheader("Personalized Recommendations")
        st.write(
            "Receive practical suggestions based on your assessment."
        )

    with st.container(border=True):
        st.subheader("Quick Assessment")
        st.write(
            "Complete the questionnaire in approximately 2–3 minutes."
        )

st.write("")

# ==========================================================
# DISCLAIMER
# ==========================================================

st.warning("""
**Disclaimer**

This application is intended for educational and research purposes only.

It is **not a medical diagnosis** and should not replace consultation with a qualified mental health professional.
""")

st.write("")
st.write("")

# ==========================================================
# START BUTTON
# ==========================================================

col1, col2, col3 = st.columns([2,1,2])

with col2:

    if st.button("Start Assessment", use_container_width=True):
        st.switch_page("pages/assessments.py")