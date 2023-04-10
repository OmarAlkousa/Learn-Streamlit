# Import the required packages
import numpy as np


# Building a class Signal for better use.
class Signal:
    """
    Generate sinusoidal signals with specific ampltiudes, frequencies, duration,
    sampling rate, and phase.

    Example:
      signal = Signal(amplitude=10, sampling_rate=2000.0)
      sine = signal.sine()
      cosine = signal.cosine()
    """

    def __init__(self, amplitude=1, frequency=1, duration=1, sampling_rate=100.0, phase=0):
        """
        Initialize the Signal class.

        Args:
            amplitude (float): The amplitude of the signal
            frequency (int): The frequency of the signal Hz
            duration (float): The duration of the signal in second
            sampling_rate (float): The sampling per second of the signal
            phase (float): The phase of the signal in radians

        Additional parameters,which are required to generate the signal, are
        calculated and defined to be initialized here too:
            time_step (float): 1.0/sampling_rate
            time_axis (np.array): Generate the time axis from the duration and
                                  the time_step of the signal. The time axis is
                                  for better representation of the signal.
        """
        self.amplitude = amplitude
        self.frequency = frequency
        self.duration = duration
        self.sampling_rate = sampling_rate
        self.phase = phase
        self.time_step = 1.0/self.sampling_rate
        self.time_axis = np.arange(0, self.duration, self.time_step)

    # Generate sine wave
    def sine(self):
        """
        Method of Signal

        Returns:
            np.array of sine wave using the pre-defined variables (amplitude,
            frequency, time_axis, and phase)
        """
        return self.amplitude*np.sin(2*np.pi*self.frequency*self.time_axis+self.phase)

    # Generate cosine wave
    def cosine(self):
        """
        Method of Signal

        Returns:
            np.array of cosine wave using the pre-defined variables (amplitude,
            frequency, time_axis, and phase)
        """
        return self.amplitude*np.cos(2*np.pi*self.frequency*self.time_axis+self.phase)
