# Import the required packages
import streamlit as st
import numpy as np
import io


def download(signal, filename='signal.csv'):
    # Create an in-memory buffer
    with io.BytesIO() as buffer:
        # Write array to buffer
        np.savetxt(buffer, signal, delimiter=",", fmt='%.18f')
        st.download_button(label="Download array as CSV",
                           data=buffer,  # Download buffer
                           file_name=filename,
                           mime='text/csv')
