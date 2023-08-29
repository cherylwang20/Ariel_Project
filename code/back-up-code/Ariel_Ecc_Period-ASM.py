'''
@author: Huiyi (Cheryl) Wang
August 2023

This code looks the distribution of Ariel Targets
Ariel-Phasecurves- Period - Eccentricity - ASM

'''


from phasecurve_plot_cheryl import *
import matplotlib

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel.ASM.min(), ariel.ASM.max()
# cmap='viridis_r'
cmap = 'hot_r'


##
Ariel_terr = ax.scatter(ariel_terrestrial["Planet Period [days]"], ariel_terrestrial['Eccentricity'],
                        alpha=0.6, s = 50, c = ariel_terrestrial["ASM"], marker="o",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "Terrestrial", zorder = 4)

Ariel_subnep = ax.scatter(ariel_subnep["Planet Period [days]"], ariel_subnep['Eccentricity'],
                        alpha=0.6, s = 150, c = ariel_subnep["ASM"], marker="o",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "SubNeptune", zorder = 3)

Ariel_nept = ax.scatter(ariel_nep["Planet Period [days]"], ariel_nep['Eccentricity'],
                        alpha=0.6, s = 400, c = ariel_nep["ASM"], marker="o",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "Neptune", zorder = 2)

Ariel_giant = ax.scatter(ariel_giant["Planet Period [days]"], ariel_giant['Eccentricity'],
                        alpha=0.6, s = 600, c = ariel_giant["ASM"], marker="o",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "Giant", zorder = 1)


# ax.set_clim(min_, max_)
clb = fig.colorbar(Ariel_terr, ax=ax)  # .set_label('$\\bf{ASM} $',rotation=270,fontsize=15)
clb.ax.set_title('$\\bf{ASM} $')

# Create a legend for the first line.
# first_legend = plt.legend(handles=[Spitzer_plot,Hubble_plot, JWST_plot], loc='upper right',
#                           title = "$\\bf{Telescope} $", title_fontsize = 20, prop={'size': 20}, fancybox = True)

ax.axvline(3, color='red', linestyle='dashed', linewidth=2, alpha=0.75, zorder = 0)

from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='*', color='w', label='Terrestrial',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                    Line2D([0], [0], marker='o', color='w', label='Sub-Neptune',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=20),
                    Line2D([0], [0], marker='p', color='w', label='Neptune',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                    Line2D([0], [0], marker='+', color='w', label='Giant',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25)
                   ]


plt.grid(True, alpha=0.35)
plt.xlabel("Planet Period [days]", fontsize=18, fontweight='bold')
plt.ylabel("Eccentricity", fontsize=18, fontweight='bold')
plt.title("Ariel Phase Curve Targets: Period vs Eccentricity", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.gca().set_ylim(top=1)
#plt.yscale('log')
plt.xscale('log')
#plt.ylim([0,1])
#plt.xlim([1,100])
plt.savefig(save_dir+'Ariel-Phasecurves-Per-Ecc-ASM.jpg')

plt.show()