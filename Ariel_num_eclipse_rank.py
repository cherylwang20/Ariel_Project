from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))

min_, max_ = ariel_sort_ESM['Planet Radius [Rj]'].min(), ariel_sort_ESM['Planet Radius [Rj]'].max()
# cmap='viridis_r'
cmap = 'PiYG'

print(len(ariel_sort_ESM))

Ariel_plot = ax.scatter(ariel_sort_eclipse_num.index.tolist(), ariel_sort_eclipse_num['ESM'],
                        alpha=0.9, s = 50, c = ariel_sort_eclipse_num['Planet Radius [Rj]'], marker="o",
                        label = "Ariel", zorder = 1)

clb = fig.colorbar(Ariel_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planet Radius [Rj]',fontsize=16)

plt.grid(True, alpha=0.35)
plt.xlabel("Planet Rank", fontsize=18)
plt.ylabel("Emission Spectroscopy Metric", fontsize=18)
plt.title("Ariel Phase Curve Targets - # eclipse Ranked", fontsize=24)
plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-PhaseCurve-Eclipse-Planet-Rank.jpg')

plt.show()