import numpy as np
import matplotlib.pyplot as plt
import os.path
import matplotx
data_dir = os.path.join(os.getcwd(), 'data/')


from astropy.modeling.models import BlackBody
from astropy import units as u
import pandas as pd
from astropy.visualization import quantity_support

from function_constants import *

bb = BlackBody(temperature=5778*u.K, scale = 1)

flux = bb(7.5*u.micron)
flux_2 = planck(5778)

#print(flux.to(u.W/u.m**2/u.steradian/u.Hz)*c/wav**2)
#print(flux)
#print(flux_2)

### choose a few targets, 3 - 5 for referencing their change in value based on their ASM ranking.

targets = pd.read_csv(os.path.join(data_dir, 'four_target.csv'))

#### check the two instrument that Ariel have
## AIRS  is  the  Ariel  scientific  instrument providing  low-resolution  spectroscopy  in  two  IR  channels
# (called Channel 0, CH0, for the [1.95-3.90] μm band and Channel 1, CH1, for the [3.90-7.80] μm band).
# NIRSpec (1.10-1.95 μm spectrometer with R ≥ 15)

targets['Transit Signal'] = transit_signal(targets['Planet Radius [Rj]'], T_day_eff(targets['Star Temperature [K]'],
                                            targets['Star Radius [Rs]'], targets['Planet Semi-major Axis [m]']),
                                            targets['pl_g'],targets['Star Radius [Rs]'])

#print(targets['Transit Signal'])

print(transit_signal(1.1, 1787 ,20, 0.75, 4))

#### emission spectroscopy signal, in range of ariel

ariel_wl_sig = np.arange(1.10, 7.90, 0.1)*1e-6

target_emiss = []
all_emiss = []

fig, ax = plt.subplots(figsize=(15, 10))


for i, row in targets.iterrows():
    target_emiss = []
    for j in ariel_wl_sig:
        target_emiss.append(ASM_astropy(row['Planet Radius [Rj]'],row['Star Radius [Rs]'], T_day_eff(row['Star Temperature [K]'],
                                            row['Star Radius [Rs]'], row['Planet Semi-major Axis [m]']),row['Star Temperature [K]'], j))
    plt.plot(ariel_wl_sig*10**6, target_emiss, label = row['Planet Name'], linewidth = 3)
    all_emiss.append(target_emiss)

plt.grid(True, alpha=0.35)
plt.text(1.2, 1e-2, 'NIRSpec', fontweight='bold',fontsize=14)
plt.text(2.5, 1e-2, 'AIRS CH0', fontweight='bold',fontsize=14)
plt.text(5, 1e-2, 'AIRS CH1', fontweight='bold',fontsize=14)
ax.axvspan(1.1, 1.95, alpha=0.2, color='green')
ax.axvspan(1.95, 3.9, alpha=0.2, color='yellow')
ax.axvspan(3.9, 7.8, alpha=0.2, color='pink')


plt.title('Ariel Target: Emission Signal vs Wavelength',fontsize=24, fontweight='bold')
plt.ylabel('Thermal Contrast',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#matplotx.line_labels()
plt.legend()
#plt.xscale('log')
plt.yscale('log')
plt.savefig(save_dir + 'Ariel_Emission_Wavelength.jpg')
#plt.show()
plt.close()

