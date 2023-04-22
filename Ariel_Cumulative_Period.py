from phasecurve_plot_cheryl import *
import matplotlib

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel.ESM.min(), ariel.ESM.max()
print(min_,max_)
# cmap='viridis_r'
cmap = 'cool'

Ariel_plot = ax.scatter(ariel["Planet Temperature [K]"], ariel['Cumulative time (days)'],
                        alpha=0.8, s = 100, c = ariel["ESM"], marker="*",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "Ariel", zorder = 1)

# ax.set_clim(min_, max_)
clb = fig.colorbar(Ariel_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
clb.ax.set_title('$\\bf{ESM} $')

ax.axhline(100, color='r', linestyle='dashed', linewidth=1, alpha=1)
# Create a legend for the first line.
# first_legend = plt.legend(handles=[Spitzer_plot,Hubble_plot, JWST_plot], loc='upper right',
#                           title = "$\\bf{Telescope} $", title_fontsize = 20, prop={'size': 20}, fancybox = True)


from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='*', color='w', label='Ariel',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25)
                   ]

first_legend = plt.legend(handles=legend_elements, loc='upper right',
                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)

# # Create another legend for the second line.
# plt.legend(handles=[eccen_plot], loc='lower right',
#           title = "$\\bf{Eccentric \ Planets}$", title_fontsize = 15, prop={'size': 15}, fancybox = True)

plt.grid(True, alpha=0.35)
plt.xlabel("Planetary Equilibrium Temperature [K]", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Planet Orbital Period [days]", fontsize=18, fontweight='bold')
plt.title("Planets Observed with Phase Curves", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-ESM-T_Cul.jpg')

plt.show()