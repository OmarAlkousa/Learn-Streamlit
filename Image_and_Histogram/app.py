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

#################
# Documentation #
#################
# Set a title of the app
st.markdown("<h1 style='text-align: center; color: grey;'>Image & Histogram</h1>",
            unsafe_allow_html=True)
# Explanation of the web app
st.markdown('''
This web app is to represent how you can use streamlit to import local RGB images and show its histogram.
All you have to do is to upload the image file.
            ''')

# Fast Example of the app
st.markdown("### Import the image file")
st.markdown("If you want a fast try of this app and you don't have any image file, you can download an example file ('Your Name.jpg') that is in the same \
            [**GitHub repository**](https://github.com/OmarAlkousa/Learn-Streamlit/blob/cf6055fbc1bafe416285924c1d196bf3dacc02c0/Image_and_Histogram/Your%20Name.jpg) \
            of the app.")


###################
# Upload an image #
###################
uploaded_file = st.file_uploader(
    label="Import the file of the image")

# If the file is uploaded
if uploaded_file is not None:

    # Caching the data for faster implementation
    @st.cache_data
    def load_image():
        img = Image.open(uploaded_file.name)
        img_array = np.array(img)
        return img, img_array

    # Load the Data
    img, img_array = load_image()

    #################
    # Display Image #
    #################
    fig1 = px.imshow(img=img, aspect='auto')

    # Layout configuration
    fig1.update_layout({"title": {"text": 'Image',
                                  "font": {"size": 30, "family": "Times New Roman, bold"},
                                  "x": 0.5,
                                  "xanchor": "center",
                                  "yanchor": "top"},
                        "xaxis": {"title": 'Pixel'},
                        "yaxis": {"title": 'Pixel'}})

    # Show the image plot
    st.plotly_chart(fig1, theme="streamlit", use_container_width=False)

    #####################
    # Display Histogram #
    #####################
    fig2 = make_subplots(1, 1)
    # Histogram for each color channel
    for channel, color in enumerate(['red', 'green', 'blue']):
        fig2.add_trace(go.Histogram(x=img_array[..., channel].ravel(), opacity=0.5,
                                    marker_color=color, name='%s channel' % color), 1, 1)

    # Layout configuration
    fig2.update_layout({"title": {"text": 'Histogram',
                                  "font": {"size": 30, "family": "Times New Roman, bold"},
                                  "x": 0.5,
                                  "xanchor": "center",
                                  "yanchor": "top"},
                        "xaxis": {"title": 'Intenstiy'},
                        "yaxis": {"title": 'Count'}})

    # Show the histogram plot
    st.plotly_chart(fig2, theme="streamlit", use_container_width=False)
