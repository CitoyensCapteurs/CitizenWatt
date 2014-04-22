#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.integrate import trapz

# Load data
with open('sample.log', 'r') as fh:
    lines = fh.readlines() 
    signal = np.zeros(len(lines))
    i = 0
    for line in lines:
        signal[i] = line.split(' ')[0]
        i += 1

t = np.arange(0, len(lines)*5, 5)

total = trapz(signal) / 1000 / 3600 * 5 # 5 is timestep

fig = plt.figure()
fig.suptitle('Puissance totale : '+str(round(total, 3)) +' kWh', y=0.03, x=0.55,
             bbox=dict(facecolor='yellow', edgecolor='black'))
ax1 = fig.add_subplot('211')
ax1.plot(t, signal)
ax1.set_xticks(np.arange(7200,200000,86400))
ax1.set_xticklabels([str(int(i/86400 * 24)) + "h" for i in np.arange(0,200000,86400)])
ax1.xaxis.set_minor_locator(AutoMinorLocator(24))
ax1.set_title('Données complètes')
ax1.set_xlabel('Temps')
ax1.set_ylabel('Puissance (en W)')
ax1.grid(b=True, which='major', color='black', linestyle='-')
ax1.grid(b=True, which='minor', color='black', linestyle='--', alpha=0.2)

t = t[1440:18720]
signal = signal[1440:18720]
ax2 = fig.add_subplot('212')
ax2.plot(t, signal)
ax2.set_xticks(np.arange(7200,86400+7200,3600))
ax2.set_xticklabels([str(int(i/3600)) + "h" for i in np.arange(0,86400+7200,3600)])
ax2.set_title('Zoom sur une journée')
ax2.set_xlabel('Temps')
ax2.set_ylabel('Puissance (en W)')
ax2.grid(b=True, which='major', color='black', linestyle='-')

plt.tight_layout()
plt.show()
