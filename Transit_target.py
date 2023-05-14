from phasecurve_plot_cheryl import *


fig, ax = plt.subplots(figsize=(15, 10))

overlap_time_day = overlap_target['cumulative transit time [days]'].tolist()

Ariel_transit = ax.plot(overlap_target.index.tolist(), overlap_time_day,
                        alpha = 1, linewidth= 3)

#ax.axhline(120, color='orange', linestyle='solid', linewidth=2, alpha=0.75, zorder = 0)


#ax.legend(loc='lower right',
#                          title="$\\bf{Sorting Parameter} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
#ax = plt.gca().add_artist(first_legend)

# # Create another legend for the second line.
# plt.legend(handles=[eccen_plot], loc='lower right',
#           title = "$\\bf{Eccentric \ Planets}$", title_fontsize = 15, prop={'size': 15}, fancybox = True)

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
plt.title("Ariel Phase Curve Cumulative Transit Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Cul_Transit.jpg')

plt.show()







