'''
@author: Huiyi (Cheryl) Wang
August 2023

Backup code
calculates the temperature different between day/night time of 16 selected targets
in Taylor's Spitzer reanalysis paper
'''


import matplotlib.pyplot as plt

from phasecurve_plot_cheryl import *
fig  = plt.subplots(figsize=(8, 6))

plt.scatter(selected_sample['Planet Temperature [K]'], selected_sample['T day (K)'], label = 'Day', color = 'orange')
plt.scatter(selected_sample['Planet Temperature [K]'], selected_sample['T night (K)'], label = 'Night', color = 'blue')
plt.legend()
plt.xlabel('Planet Equilibrium Temperature [K]')
plt.ylabel('Planet Day/Night Side Temperature [K]')
plt.grid(True, alpha=0.35)

plt.savefig(save_dir + 'Day-Night Temp vs T_eq.jpg')
plt.show()

same_night = pd.read_excel(data_dir + 'selected_target_same_stellar.xlsx')

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = same_night['Planet Radius [Rj]'].min(), same_night['Planet Radius [Rj]'].max()

cmap = 'PiYG'

same_night['ESM High'] = ESM(same_night['T day (K)'], same_night["Star Temperature [K]"], same_night["Planet Radius [Rj]"],
                   same_night["Star Radius [Rs]"], same_night["Star K Mag"])
same_night['ESM Low'] = ESM(same_night['T night (K)'], same_night["Star Temperature [K]"], same_night["Planet Radius [Rj]"],
                   same_night["Star Radius [Rs]"], same_night["Star K Mag"])



Ariel_target_ESM_Day = ax.scatter(same_night['Planet Temperature [K]'], same_night['ESM High']/same_night['ESM Low'],
                                    alpha=1, s=250, c=same_night['Planet Radius [Rj]'], marker="o", edgecolor='black',
                                    zorder=2, cmap = cmap, vmin=min_, vmax=max_
                                    )

plt.xticks(rotation=45)

clb = fig.colorbar(Ariel_target_ESM_Day, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planet Radius [Rj]',fontsize=16)




plt.grid(True, alpha=0.35)
plt.xlabel("Planet Equilibrium Temperature", fontsize=18)
plt.ylabel("ESM Day to Night Ratio", fontsize=18)
plt.title("Ariel Phase Curve Targets: ESM ratio vs T_eq, Night ~1100K", fontsize=24)
#plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-PhaseCurve-ESM-ratio-same-night.jpg')

plt.show()