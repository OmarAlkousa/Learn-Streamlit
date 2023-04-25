# License: MIT
# Author: Omar Alkousa
# Email: omar.ok1998@gmail.com
# LinkedIn: linkedin.com/in/omar-alkousa/
# Medium: medium.com/@omar.ok1998


# Import the required package
import streamlit as st
from PIL import Image
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import cv2

#################
# Documentation #
#################
# Set a title of the app
st.markdown("<h1 style='text-align: center; color: grey;'>Thresholding Medical Images/h1>",
            unsafe_allow_html=True)
# Explanation of the web app
st.markdown('''
This web app is to represent how you can use streamlit to import local Grayscale images and show its histogram to specify the threshold you want to apply.
All you have to do is to upload the image file.
            ''')

# Fast Example of the app
st.markdown("### Import the image file")
st.markdown("If you want a fast try of this app and you don't have any image file, you can download an example file that is in the same \
            [**GitHub repository**](https://github.com/OmarAlkousa/Learn-Streamlit/blob/ec0163bae4aa90e7c38ae252f834a50afc5d007a/Thresholding%20in%20Medical%20Images/Lung.jpg) of the app.")


###################
# Upload an image #
###################
uploaded_file = st.file_uploader(label="Import the file of the image")

# If the file is uploaded
if uploaded_file is not None:

    # Caching the data for faster implementation
    @st.cache_data
    def load_image():
        img = cv2.imread(uploaded_file.name, flags=cv2.IMREAD_GRAYSCALE)
        return img

    # Load the Data
    img = load_image()


    #####################
    # Display Histogram #
    #####################
    fig1 = make_subplots(1, 1)
    # Histogram
    fig1.add_trace(go.Histogram(x=img.ravel(), opacity=0.5), 1, 1)

    # Layout configuration
    fig1.update_layout({'title': {'text': 'Histogram',
                                  'font': {'size': 30, 'family': 'Times New Roman, bold'},
                                  'x': 0.5,
                                  'xanchor': 'center',
                                  'yanchor': 'top'},
                        'xaxis': {'title': 'Intenstiy'},
                        'yaxis': {'title': 'Count'}})
    
    # Specify the threshold
    threshold = st.slider(label='Specify the Threshold [0 ~ 255]',
                          min_value=0,
                          max_value=255,
                          value=round(img.mean()))

    # Plot a vertical line that represents the specified threshold
    fig1.add_vline(x=threshold, line_width=1, line_color='red')

    # Show the histogram plot
    st.plotly_chart(fig1, theme='streamlit', use_container_width=False)

    # Apply the threshold on the image
    ret, thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    # Plot the original and the image after applying the threshold
    column1, column2 = st.columns(2)
    

    #################
    # Display Image #
    #################
    fig2 = px.imshow(img=img, color_continuous_scale='gray')

    # Layout configuration
    fig2.update_layout({'title': {'text': 'Original Image',
                                  'font': {'size': 30, 'family': 'Times New Roman, bold'},
                                  'x': 0.5,
                                  'xanchor': 'center',
                                  'yanchor': 'top'},
                        'xaxis': {'title': None, 'showticklabels':False},
                        'yaxis': {'title': None, 'showticklabels':False},
                        'coloraxis_showscale':False})

    # Show the image plot
    column1.plotly_chart(fig2, theme='streamlit', use_container_width=True)
    
    # Display Image after applying the specified threshold
    fig3 = px.imshow(img=thresh, color_continuous_scale='gray')

    # Layout configuration
    fig3.update_layout({'title': {'text': 'Image after Threshold',
                                  'font': {'size': 30, 'family': 'Times New Roman, bold'},
                                  'x': 0.5,
                                  'xanchor': 'center',
                                  'yanchor': 'top'},
                        'xaxis': {'title': None, 'showticklabels':False},
                        'yaxis': {'title': None, 'showticklabels':False},
                        'coloraxis_showscale':False})

    # Show the image plot
    column2.plotly_chart(fig3, theme="streamlit", use_container_width=True)
