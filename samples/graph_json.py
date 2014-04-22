#!/usr/bin/env python

import json
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.integrate import trapz

# Load data
with open('sample2', 'r') as fh:
    raw = json.loads(fh.read())['Serie']

signal = []
t_signal = []
t_battery = []
battery = []

t0 = raw[0]['timestamp']
i = True

for measure in raw:
    if measure['timestamp'] == 0:
        continue

    t_signal.append(measure['timestamp'] - t0)
    signal.append(measure['measure'])

    if measure['measure'] != measure['battery']:
        if i:
            t1 = measure['timestamp']
            i = False
        t_battery.append(measure['timestamp'] - t1)
        battery.append(measure['battery'])


total = trapz(signal) / 1000 / 3600 * 5 # 5 is timestep

fig = plt.figure()
fig.suptitle('Énergie totale : '+str(round(total, 3)) +' kWh', y=0.03, x=0.55,
             bbox=dict(facecolor='yellow', edgecolor='black'))
ax1 = fig.add_subplot('211')
ax1.text(s=time.strftime("%H:%M %D", time.localtime(t0)), y=-75, x=-7500)
ax1.plot(t_signal, signal)
ax1.set_xticks(np.arange(0,90000,86400))
ax1.set_xticklabels([str(int(i/86400 * 24)) + "h" for i in np.arange(0,90000,86400)])
ax1.xaxis.set_minor_locator(AutoMinorLocator(24))
ax1.set_title('Données complètes')
ax1.set_xlabel('Temps')
ax1.set_ylabel('Puissance (en W)')
ax1.grid(b=True, which='major', color='black', linestyle='-')
ax1.grid(b=True, which='minor', color='black', linestyle='--', alpha=0.2)

ax2 = fig.add_subplot('212')
ax2.plot(t_battery, battery)
ax2.text(s=time.strftime("%H:%M %D", time.localtime(t0)), y=2825, x=-2500)
ax2.set_xticks(np.arange(0,43200,3600))
ax2.set_xticklabels([str(int(i/3600)) + "h" for i in np.arange(0,43200,3600)])
ax2.set_title('Batterie')
ax2.set_xlabel('Temps')
ax2.set_ylabel('Tension (en mV)')
ax2.grid(b=True, which='major', color='black', linestyle='-')

plt.tight_layout()
plt.show()
