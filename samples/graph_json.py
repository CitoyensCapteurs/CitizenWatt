#!/usr/bin/env python3

import argparse
import json
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.integrate import trapz


parser = argparse.ArgumentParser(description="Plotting samples")
parser.add_argument('--min', default=None, type=int,
                                help="min value for timestamp")
parser.add_argument('--max', default=None, type=int,
                                help="max value for timestamp")
parser.add_argument('file', help="JSON file")
args = parser.parse_args()

# Load data
with open(sys.argv[1], 'r') as fh:
    raw = json.loads(fh.read())
raw = raw[next(iter(raw))]

battery = []
signal = []
t = []

t0 = 0

# Sort by increasing timestamp
raw = sorted(raw, key=lambda k: k['timestamp'])

# Add measures
for measure in raw:
    if args.min != None and  measure['timestamp'] < args.min:
        continue
    if args.max != None and measure['timestamp'] > args.max:
        continue

    if t0 == 0:
        t0 = measure['timestamp']

    t.append(measure['timestamp'] - t0)
    signal.append(measure['measure'])
    battery.append(measure['battery'])

# Integrate
total = 0
for key in range(len(t) - 1):
    total += (signal[key] + signal[key + 1]) * (t[key + 1] - t[key]) / 2
total = total / 1000 / 3600

# Plot
fig = plt.figure()
fig.suptitle('Énergie totale : '+str(round(total, 3)) +' kWh', y=0.03, x=0.55,
             bbox=dict(facecolor='yellow', edgecolor='black'))
ax1 = fig.add_subplot('211')
ax1.text(s=time.strftime("%H:%M %D", time.localtime(t0)), y=-75, x=-7500)
ax1.plot(t, signal)
days = t[-1]//86400
ax1.set_xticks(np.arange(0,days*86400,86400))
ax1.set_xticklabels([str(int(i/86400 * 24)) + "h" for i in np.arange(0,days*86400,86400)])
ax1.xaxis.set_minor_locator(AutoMinorLocator(24))
ax1.set_title('Données complètes')
ax1.set_xlabel('Temps')
ax1.set_ylabel('Puissance (en W)')
ax1.grid(b=True, which='major', color='black', linestyle='-')
ax1.grid(b=True, which='minor', color='black', linestyle='--', alpha=0.2)

ax2 = fig.add_subplot('212')
ax2.plot(t, battery)
ax2.text(s=time.strftime("%H:%M %D", time.localtime(t0)), y=2575, x=-2500)
days = t[-1]//86400
ax2.set_xticks(np.arange(0,days*86400,86400))
ax2.set_xticklabels([str(int(i/3600)) + "h" for i in np.arange(0,days*86400,86400)])
ax2.xaxis.set_minor_locator(AutoMinorLocator(24))
ax2.set_title('Batterie')
ax2.set_xlabel('Temps')
ax2.set_ylabel('Tension (en mV)')
ax2.grid(b=True, which='major', color='black', linestyle='-')
ax2.set_ylim([2700,4000])

plt.tight_layout()
plt.show()
