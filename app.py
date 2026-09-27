import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ BMI Calculator")
st.write("Calculate your Body Mass Index using your weight and height.")

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    max_value=300.0,
    value=60.0,
    step=0.5
)

height = st.number_input(
    "Height (m)",
    min_value=0.5,
    max_value=2.5,
    value=1.70,
    step=0.01
)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)

    st.metric("Your BMI", f"{bmi:.2f}")

    if bmi < 18.5:
        st.info("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal range")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obesity")
