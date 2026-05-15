import streamlit as st

st.title('BMI Calculator')

weight = st.number_input('Enter your weight in kg', min_value=1.0, max_value=500.0, step=0.1)
height = st.number_input('Enter your height in meters', min_value=0.5, max_value=3.0, step=0.01)

if st.button('Calculate BMI'):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f'Your BMI is: {bmi:.2f}')
    else:
        st.write('Height must be greater than zero')
