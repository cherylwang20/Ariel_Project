'''
@author: Huiyi (Cheryl) Wang
August 2023

This compare the ESM and the Eclipse metric

Ariel-Phasecurves-ESM-Eclipse-Temperature
'''

from phasecurve_plot_cheryl import *
import matplotlib

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel['Planet Temperature [K]'].min(), ariel['Planet Temperature [K]'].max()
print(min_,max_)
# cmap='viridis_r'
cmap = 'RdYlBu_r'
#ax.axvline(3, color='red', linestyle='dashed', linewidth=2, alpha=0.75, zorder = 0)


Ariel_terr = ax.scatter(ariel_terrestrial['Tier 3 Eclipses'],ariel_terrestrial["ESM"],
                        alpha=0.6, s = 50, c = ariel_terrestrial["Planet Temperature [K]"], marker="o",
                        edgecolor='black', cmap=cmap, vmin=min_, vmax=max_,
                        linewidths=0.6, label = "Terrestrial", zorder = 4)

Ariel_subnep = ax.scatter(ariel_subnep['Tier 3 Eclipses'],ariel_subnep["ESM"],
                        alpha=0.6, s = 150, c = ariel_subnep["Planet Temperature [K]"], marker="o",
                        edgecolor='black', cmap=cmap, vmin=min_, vmax=max_,
                        linewidths=0.6, label = "SubNeptune", zorder = 3)

Ariel_nept = ax.scatter( ariel_nep['Tier 3 Eclipses'],ariel_nep["ESM"],
                        alpha=0.6, s = 400, c = ariel_nep["Planet Temperature [K]"], marker="o",
                        edgecolor='black', cmap=cmap,vmin=min_, vmax=max_,
                        linewidths=0.6, label = "Neptune", zorder = 2)

Ariel_giant = ax.scatter(ariel_giant['Tier 3 Eclipses'],ariel_giant["ESM"],
                        alpha= 0.6, s = 600, c = ariel_giant["Planet Temperature [K]"], marker="o",
                        edgecolor='black',cmap=cmap,vmin=min_, vmax=max_,
                        linewidths=1, label = "Giant", zorder = 2)


# ax.set_clim(min_, max_)
clb = fig.colorbar(Ariel_terr, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
clb.set_label('Planetary Equilibrium Temperature [K]',fontsize=20)
clb.ax.tick_params(labelsize=17)


############################################################33

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
#                          title="$\\bf{Planet Type} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
#ax = plt.gca().add_artist(first_legend)

# # Create another legend for the second line.
# plt.legend(handles=[eccen_plot], loc='lower right',
#           title = "$\\bf{Eccentric \ Planets}$", title_fontsize = 15, prop={'size': 15}, fancybox = True)

plt.grid(True, alpha=0.35)
plt.xlabel("# of Tier 3 Eclipses", fontsize=18, fontweight='bold')
plt.ylabel("ESM", fontsize=18, fontweight='bold')
#plt.title("Ariel Phase Curve Targets: ESM vs # Eclipse", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.yscale('log')
plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-Phasecurves-ESM-Eclipse-T.pdf')

plt.show()