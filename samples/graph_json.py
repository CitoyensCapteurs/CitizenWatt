#!/usr/bin/env python3

import json
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.integrate import trapz

# Load data
with open('sample3', 'r') as fh:
    raw = json.loads(fh.read())['Serie']

signal = []
t_signal = []
t_battery = []
battery = []

i = True
t0 = 0

raw.reverse()
last_t = 0

for measure in raw:
    if measure['timestamp'] < 1398527280 or measure['timestamp'] > 1399240800:
        continue
    if t0 == 0:
        t0 = measure['timestamp']
        last_t = t0

    t_signal.append(measure['timestamp'] - t0)
    signal.append(measure['measure'])

    if np.abs(last_t - measure['timestamp']) > 7:
        #print(np.abs(last_t - measure['timestamp']))
        pass
    last_t = measure['timestamp']

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
ax1.set_xticks(np.arange(0,8*86400,86400))
ax1.set_xticklabels([str(int(i/86400 * 24)) + "h" for i in np.arange(0,8*86400,86400)])
ax1.xaxis.set_minor_locator(AutoMinorLocator(24))
ax1.set_title('Données complètes')
ax1.set_xlabel('Temps')
ax1.set_ylabel('Puissance (en W)')
ax1.grid(b=True, which='major', color='black', linestyle='-')
ax1.grid(b=True, which='minor', color='black', linestyle='--', alpha=0.2)

ax2 = fig.add_subplot('212')
ax2.plot(t_battery, battery)
ax2.text(s=time.strftime("%H:%M %D", time.localtime(t0)), y=2575, x=-2500)
ax2.set_xticks(np.arange(0,8*86400,86400))
ax2.set_xticklabels([str(int(i/3600)) + "h" for i in np.arange(0,8*86400,86400)])
ax2.xaxis.set_minor_locator(AutoMinorLocator(24))
ax2.set_title('Batterie')
ax2.set_xlabel('Temps')
ax2.set_ylabel('Tension (en mV)')
ax2.grid(b=True, which='major', color='black', linestyle='-')
ax2.set_ylim([2700,4000])

plt.tight_layout()
plt.show()
