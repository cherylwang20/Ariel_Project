# Import modules
import datetime
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
from function_constants import *

phase_curve_target = pd.read_csv(os.path.join(data_dir, 'Tier_2_emission.csv'))

phase_curve_target['Star RA'] = np.deg2rad(phase_curve_target['Star RA'])
phase_curve_target['Star RA'] = np.mod(phase_curve_target['Star RA'] + np.pi, 2*np.pi) - np.pi

print(phase_curve_target['Star RA'])


ariel_target = pd.read_csv(os.path.join(data_dir, 'SNR_all_1.csv'))

ariel_target = ariel_target.sort_values(by = 'Tier1 Transit S/N',ascending=False)

ariel_transit = ariel_target[ariel_target['Tier1 Transit S/N'] > 10]

ariel_transit['Star RA'] = np.deg2rad(ariel_transit['Star RA'])
ariel_transit['Star RA'] = np.mod(ariel_transit['Star RA'] + np.pi, 2*np.pi) - np.pi

fig = plt.figure(figsize=(12, 8))

# Apply the aitoff projection and activate the grid
ax = plt.subplot(111, projection="aitoff")
plt.grid(True)

ax.scatter(ariel_transit['Star RA'], ariel_transit['Star Dec']*np.pi/180, color = 'blue', s = 120, label = 'Transit')

ax.scatter(phase_curve_target['Star RA'], phase_curve_target['Star Dec']*np.pi/180, color = 'red', s = 80, label = 'Phase Curve') 

# Set long. / lat. labels
plt.xlabel('Long. in deg', fontsize=20, fontweight='bold')
plt.ylabel('Lat. in deg',fontsize=20, fontweight='bold')
plt.legend(fontsize = 12)

# Save the figure
plt.savefig('Ariel_skymap.pdf', dpi=300)
plt.show()