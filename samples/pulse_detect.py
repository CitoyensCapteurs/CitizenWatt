#!/usr/bin/env python

import numpy as np
import pylab
from scipy.integrate import simps 
import sys

# Load data
with open('sample.log', 'r') as fh:
    lines = fh.readlines() 
    signal = np.zeros(len(lines))
    pulses = np.zeros(len(lines))
    threshold = 150
    i = 0
    for line in lines:
        signal[i] = line.split(' ')[0]
        if threshold < signal[i]:
            pulses[i] = 1
        if signal[i] < threshold:
            pulses[i] = 0
        i += 1

fridge_form = np.zeros(1123)
for i in range(373):
    fridge_form[i] = 135

fridge = np.zeros(len(lines))
for i in range(len(lines)):
    fridge[i] = fridge_form[i-int(i/1123)*1123]

t = np.arange(0, len(lines)*5, 5)
signal = signal - fridge

# Filter data -> mean over 5 consecutive measures
for k in range(1):
    filtered = np.zeros(len(signal))
    for i in range(2, len(signal) - 2):
        filtered[i] = (signal[i-2] + signal[i-1] + signal[i] + signal[i+1] +
                    signal[i+2]) / 5
    signal[2:-2] = filtered[2:-2]

pylab.plot(t, signal)
pylab.show()
sys.exit()

pylab.subplot(211)
pylab.plot(t, signal)
pylab.subplot(212)
#pylab.plot(t,pulses)
pylab.plot(t[:-1],np.diff(signal))
pylab.show()
sys.exit()

FFT = np.abs(np.fft.fft(signal))
freqs = np.fft.fftfreq(signal.size, d=t[1]-t[0])
print(1/FFT[0])

pylab.subplot(211)
pylab.plot(t, signal)
pylab.subplot(212)
pylab.plot(freqs,FFT,'x')
pylab.show()


sub_t = t[17800:18460]
sub = signal[17800:18460]

FFT = abs(np.fft.fft(sub))
freqs = np.fft.fftfreq(sub.size, sub_t[1]-sub_t[0])
print(1/FFT[0])

pylab.subplot(211)
pylab.plot(sub_t, sub)
pylab.subplot(212)
pylab.plot(freqs,FFT,'x')
pylab.show()
