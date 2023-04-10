# Import the required packages
import streamlit as st
import Signal


def select():

    ########################
    # Signal Configuration #
    ########################
    # Select the type of the signal
    select_signal = st.selectbox(label='What type of signal you want to generate',
                                 options=['sine', 'cosine'],
                                 key='s_select_signal')
    # Spectify the amplitude of the signal
    amplitude = st.number_input(
        label='Amplitude', value=1.0, key='n_amplitude')
    # Specify the frequency of the signal in Hz
    frequency = st.number_input(
        label='Frequency [Hz]', value=1.0, key='n_frequency')
    # Specify the duration of the signal in seconds
    duration = st.number_input(
        label='Duration [sec]', value=1.0, key='n_duration')
    # Specify the phase of the signal
    phase = st.number_input(label='Phase [rad]', value=0.0, key='n_phase')
    # Specify the sampling rate of the signal in Hz
    sampling_rate = st.number_input(
        label='Sampling Rate [Hz]', value=100.0, key='n_sampling_rate')

    #######################
    # Generate the signal #
    # #####################
    # Use the Signal class to generate the signal with the specified properties
    sig = Signal.Signal(amplitude=amplitude,
                        frequency=frequency,
                        duration=duration,
                        phase=phase,
                        sampling_rate=sampling_rate)
    if select_signal == 'sine':
        signal = sig.sine()
    elif select_signal == 'cosine':
        signal = sig.cosine()

    return select_signal, sig, signal
