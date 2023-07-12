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

N = 100
start = 1.10  # Start of the interval
end = 7.80  # End of the interval
interval_size = 0.5  # Size of each interval

targets = pd.read_csv(os.path.join(data_dir, 'four_target.csv'))
ariel_wl = np.arange(1.10, 7.90, interval_size)*1e-6

#print(ariel_wl)

def Noise(t, R_star, d, T_star, lamb_1, lamb_2,tau=tau_ariel, D=D_ariel):
    bb_star = BlackBody(temperature = T_star* u.K, scale=1)
    flux_star = np.sum(bb_star([lamb_1, lamb_2] * u.m))
    wav = (lamb_2 + lamb_1)/2
    flux_star = flux_star.si*c#/wav**2
    #print(flux_star)
    #B = quad(B_int, lamb_1, lamb_2, args=T_star)
    N = np.pi**2 * tau * t / h / c * (R_star * 6.957e+8 * D / 2 / (d * pctom)) ** 2 * flux_star
    #print(N)
    return N.value

##########################

# Generate the intervals and their labels
labels = []
intervals = []
current = start
while current < end:
    interval_end = min(current + interval_size, end)
    #print(current)
    intervals.append((current, interval_end))
    labels.append(f'{current:.1f}-{interval_end:.1f}')
    current += interval_size


print(labels)
#################################

all_noise = []
all_precision = []

fig, ax = plt.subplots(figsize=(15, 10))

for i, row in targets.iterrows():
    noise_wave = []
    precision = []
    for j in range(len(ariel_wl) - 1):
        num_p = N_photon(row['Transit Duration [s]'] / daytosec, row['Star Radius [Rs]'], row['Star Distance [pc]'],
                 row['Star Temperature [K]'], ariel_wl[j], ariel_wl[j + 1])
        noise_wave.append(num_p)
        precision.append(1/np.sqrt(num_p/2))
    all_noise.append(noise_wave)
    all_precision.append(precision)
    #print(noise_wave)
    #plt.plot(ariel_wl[:-1]*10**6, noise_wave, label = row['Planet Name'], linewidth = 3)
    plt.bar(range(len(noise_wave)), noise_wave, align='center',label = row['Planet Name'], alpha = 0.7)

    # Set the x-axis tick labels
    plt.xticks(range(len(noise_wave)), labels[:-1])#, rotation=45, ha='right')



plt.grid(True, alpha=0.35)
plt.title('Ariel Target: Noise vs Wavelength',fontsize=24, fontweight='bold')
plt.ylabel('# of Photons',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

#plt.xscale('log')
plt.yscale('log')
#get handles and labels
handles, plabels = plt.gca().get_legend_handles_labels()

#specify order of items in legend
order = [0, 3, 2, 1]

#add legend to plot
plt.legend([handles[idx] for idx in order],[plabels[idx] for idx in order], loc ='upper right')

plt.savefig(save_dir + 'Ariel_Noise_Wavelength.jpg')
#plt.show()
plt.close()

############ precision plot

fig, ax = plt.subplots(figsize=(15, 10))
for i, row in targets.iterrows():
    plt.bar(range(len(all_precision[0])), all_precision[i], alpha = 0.2, label = row['Planet Name'])
plt.xticks(range(len(all_precision[0])), labels[:-1])#, rotation=45, ha='right')


plt.grid(True, alpha=0.35)


#plt.ylim([1e18, 1e23])
plt.title('Ariel Target: Precision vs Wavelength',fontsize=24, fontweight='bold')
plt.ylabel('Expected Precision',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#matplotx.line_labels()
#plt.xscale('log')
plt.yscale('log')

handles, plabels = plt.gca().get_legend_handles_labels()

#specify order of items in legend
order = [0, 3, 2, 1]

#add legend to plot
plt.legend([handles[idx] for idx in order],[plabels[idx] for idx in order], loc ='upper left')


plt.savefig(save_dir + 'Ariel_Precision_Wavelength.jpg')
plt.show()
plt.close()