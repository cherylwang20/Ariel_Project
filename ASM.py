import numpy as np
from function_constants import *
from phasecurve_plot_cheryl import *


e1 = ASM(0.24, 0.7, 619, 5000)
#print(ASM(0.24, 0.2, 619, 3000))
#print(T_day_eff(5000, 0.75, 5*6.957e+8))

n1 = N_photon( 2.5, 0.7,  100, 5000, lamb_1_ariel, lamb_2_ariel)

print('snr', e1*n1/np.sqrt(n1))

print(SNR_Ariel(2.5, 0.7, 100, 5000, lamb_1_ariel, lamb_2_ariel, 0.24, 619))


fig, ax = plt.subplots(figsize=(15, 10))

Ariel_ASM = ax.scatter(ariel_sort_ASM['ASM'].head(400), ariel_sort_ASM['Tier 3 Eclipses'].head(400), 
                        alpha = 1, linewidth= 3,
                        linestyle = 'dashdot', color = 'red')


plt.grid(True, alpha=0.35)
plt.ylabel("# of Tier 3 Eclipses", fontsize=18, fontweight='bold')
plt.xlabel("ASM", fontsize=18, fontweight='bold')
plt.title("Ariel Phase Curve Comparison of SNR", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.yscale('log')
plt.xscale('log')
plt.gca().invert_xaxis()
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Compare.jpg')

plt.show()
