# Import the required packages
import numpy as np
from scipy.signal import chirp
from scipy.signal import square
from scipy.signal import sawtooth
from scipy.signal import sweep_poly


# Building a class Signal for better use.
class Signal:
    """
    Generate sinusoidal signals with specific parameters.

    Example:
      signal = Signal(amplitude=10, sampling_rate=2000.0)
      sine = signal.sine()
      cosine = signal.cosine()
    """

    def __init__(self, amplitude=1, duration=1, sampling_rate=100.0):
        """
        Initialize the Signal class.

        Args:
            amplitude (float): The amplitude of the signal
            duration (float): The duration of the signal in second
            sampling_rate (float): The sampling per second of the signal

        Additional parameters,which are required to generate the signal, are
        calculated and defined to be initialized here too:
            time_step (float): 1.0/sampling_rate
            time_axis (np.array): Generate the time axis from the duration and
                                  the time_step of the signal. The time axis is
                                  for better representation of the signal.
        """
        self.amplitude = amplitude
        self.duration = duration
        self.sampling_rate = sampling_rate
        self.time_step = 1.0/self.sampling_rate
        self.time_axis = np.arange(0, self.duration, self.time_step)

    # Generate sine wave
    def sine(self, frequency=1.0, phase=0):
        """
        Method of Signal

        Args:
            frequency (float): The frequency of the signal Hz
            phase (float): The phase of the signal in radians

        Returns:
            np.array of sine wave using the pre-defined variables
        """
        return self.amplitude*np.sin(2*np.pi*frequency*self.time_axis+phase)

    # Generate cosine wave
    def cosine(self, frequency=1.0, phase=0):
        """
        Method of Signal

        Args:
            frequency (float): The frequency of the signal Hz
            phase (float): The phase of the signal in radians

        Returns:
            np.array of cosine wave using the pre-defined variables
        """
        return self.amplitude*np.cos(2*np.pi*frequency*self.time_axis+phase)

    # Generate chirp signal
    def chrip_signal(self, frequency_start=1, frequency_end=10, method='linear', vertex=True, phase=0):
        """
        Method of Signal

        Args:
            frequency_start (float): The frequency to start the chirp [Hz]
            frequency_end (float): The frequency to end the chirp [Hz]
            method (str): Method to sweep the frequencies ['linear', 'quadratic', 'logarithmic', 'hyperbolic']
            vertex (bool): Determine whether the vertex of the parabola that is the graph of the frequency is at t=0 or t=duration
            phase (float): The phase of the signal in radians

        Returns:
            np.array of chirp wave using the pre-defined variables
        """
        return self.amplitude*chirp(t=self.time_axis,
                                    f0=frequency_start,
                                    f1=frequency_end,
                                    t1=self.duration,
                                    method=method,
                                    phi=phase*(180/np.pi),
                                    vertex_zero=vertex)

    # Generate square wave
    def square_signal(self, frequency=1.0):
        """
        Method of Signal

        Args:
            frequency (float): The frequency of the signal [Hz]

        Returns:
            np.array of square wave using the pre-defined variables
        """
        return self.amplitude*square(2 * np.pi * frequency * self.time_axis)

    # Generate sawtooth wave
    def sawtooth_signal(self, frequency=1.0):
        """
        Method of Signal

        Args:
            frequency (float): The frequency of the signal [Hz]

        Returns:
            np.array of sawtooth wave using the pre-defined variables
        """
        return self.amplitude*sawtooth(2*np.pi*frequency*self.time_axis)

    # Generate sweep poly signal
    def poly_signal(self, poly=np.poly1d(list(np.linspace(0, 1, num=4))), phase=0):
        """
        Method of Signal

        Args:
            poly (list): List of the polynomial coefficients.

        Returns:
            np.array of sweep poly signal using the pre-defined variables
        """

        return self.amplitude*sweep_poly(t=self.time_axis, poly=poly, phi=phase*(180/np.pi))
