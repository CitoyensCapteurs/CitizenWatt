#!/usr/bin/env python3

import numpy as np
import pylab
from scipy.integrate import simps 

# Load data
with open('sample.log', 'r') as fh:
    lines = fh.readlines() 
    signal = np.zeros(len(lines))
    i = 0
    for line in lines:
        signal[i] = line.split(' ')[0]
        i += 1

t = np.arange(0, len(lines)*5, 5)

# Filter data -> mean over 5 consecutive measures
filtered = np.zeros(len(lines))
for i in range(2, len(lines) - 2):
    filtered[i] = (signal[i-2] + signal[i-1] + signal[i] + signal[i+1] +
                   signal[i+2]) / 5

signal[2:-2] = filtered[2:-2]

FFT = np.abs(np.fft.fft(signal))
freqs = np.fft.fftfreq(signal.size, d=t[1]-t[0])
print(1/FFT[0])

pylab.subplot(211)
pylab.plot(t, signal)
pylab.plot([7200, 7200], [0, 3000], 'k-', lw=2)
pylab.plot([86400+7200, 86400+7200], [0, 3000], 'k-', lw=2)
pylab.plot([2*86400+7200, 2*86400+7200], [0, 3000], 'k-', lw=2)
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
