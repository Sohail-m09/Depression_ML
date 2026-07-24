import streamlit as st

st.set_page_config(
    page_title="Assessment Result",
    page_icon="📊",
    layout="wide"
)

# --------------------------
# Check whether prediction exists
# --------------------------

if "result" not in st.session_state:

    st.warning("No assessment found.")

    if st.button("Go to Assessment"):

        st.switch_page("pages/assessments.py")

    st.stop()

result = st.session_state.result

# --------------------------
# Title
# --------------------------

st.title("Depression Risk Assessment Result")

st.write("Below is the AI-generated assessment based on your responses.")

st.divider()

# --------------------------
# Prediction Section
# --------------------------

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Predicted Risk",
        result["prediction"]
    )

with col2:

    st.metric(
        "Confidence",
        result["confidence"]
    )

st.divider()

# --------------------------
# Summary
# --------------------------

st.subheader("Assessment Summary")

st.info(result["summary"])

st.divider()

# --------------------------
# Top Features
# --------------------------

st.subheader("Key Factors Influencing the Prediction")

for feature in result["top_contributing_features"]:

    st.write(
        f"• **{feature['feature']}** "
        f"(Impact Score : {feature['impact']})"
    )

st.divider()

# --------------------------
# Recommendations
# --------------------------

st.subheader("Personalized Recommendations")

if len(result["recommendations"]) == 0:

    st.success(
        "No major concerns were identified. Continue maintaining your healthy lifestyle."
    )

else:

    for rec in result["recommendations"]:

        st.write(f"• {rec}")

st.divider()

# --------------------------
# Buttons
# --------------------------

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "Take Assessment Again",
        use_container_width=True
    ):

        st.session_state.answers = {}

        st.switch_page("pages/assessments.py")

with col2:

    if st.button(
        "Return Home",
        use_container_width=True
    ):

        st.switch_page("app.py")