# Import the required packages
import streamlit as st
import numpy as np
import Signal


def select():

    ########################
    # Signal Configuration #
    ########################
    # Select the type of the signal
    select_signal = st.selectbox(label='What type of signal you want to generate',
                                 options=['sine', 'cosine',
                                          'chirp', 'square', 'sawtooth', 'frequency-swept cosine'],
                                 key='s_select_signal')
    # Specify the sampling rate of the signal in Hz
    sampling_rate = st.number_input(
        label='Sampling Rate [Hz]', value=100.0, key='n_sampling_rate')
    # Spectify the amplitude of the signal
    amplitude = st.number_input(
        label='Amplitude', value=1.0, key='n_amplitude')
    # Specify the duration of the signal in seconds
    duration = st.number_input(
        label='Duration [sec]', value=1.0, key='n_duration')

    # Parameters for sine/cosine signals
    if select_signal in ['sine', 'cosine']:
        # Specify the frequency of the signal in Hz
        frequency = st.number_input(
            label='Frequency [Hz]', value=1.0, key='n_frequency_sinusoid')
        # Specify the phase of the signal
        phase = st.number_input(
            label='Phase [rad]', value=0.0, key='n_phase_sinusoid')

    # Parameters for chirp signal
    elif select_signal == 'chirp':
        # Staring frequency
        f0 = st.number_input(label='f0 [Hz] (the frequency to start the chirp)', value=1.0, key='n_chirp_f0',
                             help='Frequency at time t=0')
        # End frequency
        f1 = st.number_input(label='f1 [Hz] (the frequency to end the chirp)', value=10.0, key='n_chirp_f1',
                             help='Frequency of the waveform at time t1 (the duration of the chirp)')
        # Method to sweep the frequencies
        method = st.selectbox(label='Method',
                              options=['linear', 'quadratic',
                                       'logarithmic', 'hyperbolic'],
                              key='s_select_method_chirp',
                              help='Determine the frequency sweep. If not given, linear is assumed.')
        # Specify the phase of the signal
        phase = st.number_input(
            label='Phase [rad]', value=0.0, key='n_phase_chirp')
        # Choose the vertex
        vertex = st.selectbox(label='vertex_zero', options=[True, False], key='s_select_vertex_chirp',
                              help="This parameter is only used when method is 'quadratic'.\
                                It determines whether the vertex of the parabola that is the graph of the frequency is at t=0 or t=t1")

    # Parameters for sine/cosine signals
    elif select_signal in ['square', 'sawtooth']:
        # Specify the frequency of the signal in Hz
        frequency = st.number_input(
            label='Frequency [Hz]', value=1.0, key='n_frequency_square')

    # Parameters for Frequency-swept cosine signal
    elif select_signal == 'frequency-swept cosine':
        # Specify the number of terms
        n = st.number_input(label='Number of terms',
                            value=4, key='n_number_poly')
        # Specify the coefficients
        p = st.experimental_data_editor(
            data=list(np.linspace(0, 1, num=n)), key='l_poly')
        # Specify the phase
        phase = st.number_input(
            label='Phase [rad]', value=0.0, key='n_phase_poly')

    #######################
    # Generate the signal #
    # #####################
    # Use the Signal class to generate the signal with the specified properties
    sig = Signal.Signal(amplitude=amplitude,
                        duration=duration,
                        sampling_rate=sampling_rate)
    # Sine signal
    if select_signal == 'sine':
        signal = sig.sine(frequency=frequency, phase=phase)
    # Cosine signal
    elif select_signal == 'cosine':
        signal = sig.cosine(frequency=frequency, phase=phase)
    # Chirp Signal
    elif select_signal == 'chirp':
        signal = sig.chrip_signal(
            frequency_start=f0, frequency_end=f1, method=method, vertex=vertex, phase=phase)
    # Square signal
    elif select_signal == 'square':
        signal = sig.square_signal(frequency=frequency)
    # Sawtooth signal
    elif select_signal == 'sawtooth':
        signal = sig.sawtooth_signal(frequency=frequency)
    # Frequency-swept cosine signal
    elif select_signal == 'frequency-swept cosine':
        signal = sig.poly_signal(poly=np.poly1d(p), phase=phase)

    return select_signal, sig, signal
