from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = selected_sample['Planet Radius [Rj]'].min(), selected_sample['Planet Radius [Rj]'].max()

cmap = 'PiYG'


Ariel_target_ESM_Day = ax.scatter(selected_sample['To (K)'], selected_sample['ESM High']/selected_sample['ESM Low'],
                                    alpha=1, s=250, c=selected_sample['Planet Radius [Rj]'], marker="o", edgecolor='black',
                                    zorder=2, cmap = cmap, vmin=min_, vmax=max_
                                    )

plt.xticks(rotation=45)

clb = fig.colorbar(Ariel_target_ESM_Day, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planet Radius [Rj]',fontsize=16)




plt.grid(True, alpha=0.35)
plt.xlabel("Planet Equilibrium Temperature", fontsize=18)
plt.ylabel("ESM Day to Night Ratio", fontsize=18)
plt.title("Ariel Phase Curve Targets: ESM ratio vs T_eq", fontsize=24)
#plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-PhaseCurve-ESM-ratio.jpg')

plt.show()