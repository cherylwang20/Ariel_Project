
'''
@author: Huiyi (Cheryl) Wang
August 2023

The distribution of Ariel target, not major plot
Temperature- Ecc - ESM
'''

import matplotlib.pyplot as plt

from phasecurve_plot_cheryl import *
import matplotlib

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel.ESM.min(), ariel.ESM.max()
print(min_,max_)
# cmap='viridis_r'
cmap = 'cool'

Ariel_terr = ax.scatter(ariel_terrestrial["Planet Temperature [K]"], ariel_terrestrial['Eccentricity'],
                        alpha=0.6, s = 50, c = ariel_terrestrial["ESM"], marker="o",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "Terrestrial", zorder = 4)

Ariel_subnep = ax.scatter(ariel_subnep["Planet Temperature [K]"], ariel_subnep['Eccentricity'],
                        alpha=0.6, s = 150, c = ariel_subnep["ESM"], marker="o",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "SubNeptune", zorder = 3)

Ariel_nept = ax.scatter(ariel_nep["Planet Temperature [K]"], ariel_nep['Eccentricity'],
                        alpha=0.6, s = 400, c = ariel_nep["ESM"], marker="o",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "Neptune", zorder = 2)

Ariel_giant = ax.scatter(ariel_giant["Planet Temperature [K]"], ariel_giant['Eccentricity'],
                        alpha=0.6, s = 600, c = ariel_giant["ESM"], marker="o",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "Giant", zorder = 1)



clb = fig.colorbar(Ariel_terr, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
clb.ax.set_title('$\\bf{ESM} $')

# Create a legend for the first line.
# first_legend = plt.legend(handles=[Spitzer_plot,Hubble_plot, JWST_plot], loc='upper right',
#                           title = "$\\bf{Telescope} $", title_fontsize = 20, prop={'size': 20}, fancybox = True)


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

#first_legend = plt.legend(handles=legend_elements, loc='upper right',
#                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
#ax = plt.gca().add_artist(first_legend)

# # Create another legend for the second line.
# plt.legend(handles=[eccen_plot], loc='lower right',
#           title = "$\\bf{Eccentric \ Planets}$", title_fontsize = 15, prop={'size': 15}, fancybox = True)

plt.grid(True, alpha=0.35)
plt.xlabel("Planetary Equilibrium Temperature [K]", fontsize=18, fontweight='bold')
plt.ylabel("Eccentricity", fontsize=18, fontweight='bold')
plt.title("Ariel Phase Curve Targets: Temp vs Ecc", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.gca().set_ylim(top=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.ylim([0,1])
plt.savefig(save_dir+'Ariel-Phasecurves-T-Ecc.jpg')

plt.show()