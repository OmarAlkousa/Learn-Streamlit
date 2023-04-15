# Import the required packages
import streamlit as st


def add():
    # Set a title of the app
    st.markdown("<h1 style='text-align: center; color: grey;'>Signal Generator</h1>",
                unsafe_allow_html=True)
    # Explanation of the web app
    st.markdown('''
    This web app is to represent how you can use streamlit to interactively generate signals using Numpy and Scipy packages. Also, you can download the
    generated signal as a csv file.
            ''')
