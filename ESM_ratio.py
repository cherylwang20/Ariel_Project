import matplotlib.pyplot as plt

from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = selected_sample['Planet Radius [Rj]'].min(), selected_sample['Planet Radius [Rj]'].max()

cmap = 'PiYG'
x = selected_sample['Planet Temperature [K]'].values
y = selected_sample['ESM High'].values/selected_sample['ESM Low'].values

print(x, y)

coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef)
print(coef)

Ariel_target_ESM_Day = ax.scatter(selected_sample['Planet Temperature [K]'], selected_sample['ESM High']/selected_sample['ESM Low'],
                                    alpha=1, s=250, c=selected_sample['Planet Radius [Rj]'], marker="o", edgecolor='black',
                                    zorder=2, cmap = cmap, vmin=min_, vmax=max_
                                    )

plt.plot(x, poly1d_fn(x), '--k')

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