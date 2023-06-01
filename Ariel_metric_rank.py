from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))

min_, max_ = ariel_sort_ASM['Planet Radius [Rj]'].min(), ariel_sort_ASM['Planet Radius [Rj]'].max()
# cmap='viridis_r'
cmap = 'PiYG'

Ariel_plot = ax.scatter(ariel_sort_ASM.index.tolist(), ariel_sort_ASM['ASM'],
                        alpha=0.9, s = 50, c = ariel_sort_ASM['Planet Radius [Rj]'], marker="o",
                        label = "Ariel", zorder = 1)
print(ariel_sort_ASM['ASM'])
clb = fig.colorbar(Ariel_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planet Radius [Rj]',fontsize=16)

plt.grid(True, alpha=0.35)
plt.xlabel("Planet Rank", fontsize=18)
plt.ylabel("Ariel SNR Metric", fontsize=18)
plt.title("Ariel Phase Curve Targets - ASM Ranked", fontsize=24)
plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-PhaseCurve-ASM-Rank.jpg')

plt.show()
