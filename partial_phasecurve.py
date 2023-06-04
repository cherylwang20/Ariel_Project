from phasecurve_plot_cheryl import *

# we define the angle region when which we need to observe
# before and after the eclipse to account for phase curve offset
angle = [45, 60, 80, 90]

partial_cutoff = 150

# we filter out things that are smaller than 2 days
# and we take a partial curve of all greater than 2 days, with the angle we defined

############this is ranked by Tier 3 eclipses

fig, ax = plt.subplots(figsize=(15, 10))

for i in angle:
    curve_df, fc, pc = new_cum_time(ariel_sort_eclipse_num,i)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')


ariel_sort_eclipse_num_2 = ariel_sort_eclipse_num[ariel_sort_eclipse_num['cumulative days'] < partial_cutoff]

Ariel_eclipse = ax.plot(ariel_sort_eclipse_num_2.index.tolist(), ariel_sort_eclipse_num_2['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       color = 'black')


ax.axhline(120, color='orange', linestyle='solid', linewidth=2, alpha=0.75, zorder = 0)


plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (Tier 3 Eclipse Ranked)", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
plt.title("Ariel Partial Phase Curve (> 48hr) Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = "Partial Observing Angle (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Cul-Eclipse.jpg')

plt.show()
plt.close()


############this is ranked by ASM

fig, ax = plt.subplots(figsize=(15, 10))

for i in angle:
    curve_df, fc, pc = new_cum_time(ariel_sort_ASM,i)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')


ariel_sort_ASM_2 = ariel_sort_ASM[ariel_sort_ASM['cumulative days'] < partial_cutoff]

Ariel_ASM = ax.plot(ariel_sort_ASM_2.index.tolist(), ariel_sort_ASM_2['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       color = 'black')


ax.axhline(120, color='orange', linestyle='solid', linewidth=2, alpha=0.75, zorder = 0)


plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (ASM Ranked)", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
plt.title("Ariel Partial Phase Curve (> 48hr) Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = "Partial Observing Angle (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Cul-ASM-partial.jpg')

plt.show()
plt.close()