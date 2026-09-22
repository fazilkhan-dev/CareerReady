import streamlit as st

st.set_page_config(
    page_title="CareerReady",
    page_icon="🎯",
    layout="wide"
)

st.title("CareerReady")

st.subheader("A Smart Placement Readiness System for Students")

st.write(
    "CareerReady helps students understand their preparation "
    "for a target job role and identify what they should improve."
)

st.info("Current target role: Data Analyst")

st.success("CareerReady application is running!")