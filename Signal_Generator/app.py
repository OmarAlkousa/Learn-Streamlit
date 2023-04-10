# Import the required packages
import streamlit as st
import documentation
import select_signal
import viz_signal
import download_signal

###############################
# Add Title and Documentation #
###############################
documentation.add()

######################################
# Signal Selection and Configuration #
######################################
signal_type, properties, signal = select_signal.select()

#####################################
# Download the signal as a CSV file #
#####################################
download_signal.download(signal=signal)

#################
# Visualization #
#################
fig = viz_signal.visualize(x=properties.time_axis,
                           y=signal,
                           title=signal_type.capitalize() + ' Wave')

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
