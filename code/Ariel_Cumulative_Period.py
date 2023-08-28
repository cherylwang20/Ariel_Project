from phasecurve_plot_cheryl import *
import matplotlib

fig, ax = plt.subplots(figsize=(15, 10))

Ariel_so = ax.plot(ariel_sort_so.index.tolist(), ariel_sort_so['cumulative days'].tolist(),
                        alpha=0.8, label = "Orbital Period", linewidth= 3,
                        linestyle = 'dashed', color = 'green')

Ariel_ESM = ax.plot(ariel_sort_ESM.index.tolist(), ariel_sort_ESM['cumulative days'].tolist(),
                         alpha = 1, label = "ESM", linewidth= 3,
                        linestyle = 'solid', color = 'yellow')

Ariel_eclipse = ax.plot(ariel_sort_eclipse_num.index.tolist(), ariel_sort_eclipse_num['cumulative days'].tolist(),
                        alpha = 1, label = "# Eclipse", linewidth= 3,
                        linestyle = 'dashdot', color = 'red')

Ariel_ASM = ax.plot(ariel_sort_ASM.index.tolist(), ariel_sort_ASM['cumulative days'].tolist(),
                        alpha = 1, label = "ASM", linewidth= 3,
                        linestyle = 'dotted', color = 'blue')

ax.axhline(120, color='orange', linestyle='solid', linewidth=2, alpha=0.75, zorder = 0)


ax.legend(loc='lower right',
                          title="$\\bf{Sorting Parameter} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
#ax = plt.gca().add_artist(first_legend)

# # Create another legend for the second line.
# plt.legend(handles=[eccen_plot], loc='lower right',
#           title = "$\\bf{Eccentric \ Planets}$", title_fontsize = 15, prop={'size': 15}, fancybox = True)

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
plt.title("Ariel Phase Curve Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Cul_Orb.jpg')

plt.show()