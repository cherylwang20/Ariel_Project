from phasecurve_plot_cheryl import *

###### we look at the 51 Tier 2 emission spectroscopy targets calculate by Ariel_tiers_calculation.py
tier_2_indice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 47, 48, 50, 52, 53, 54, 57, 60]

tier2_targets = ariel.iloc[tier_2_indice]

tier2_eclipse_sort = tier2_targets.sort_values('Tier 2 Eclipses')
cum_time = []
cum = 0
for index, row in tier2_eclipse_sort.iterrows():
    cum += row['Planet Period [days]'] + 2*row['Transit Duration [s]']/ 86400
    cum_time.append(cum)

tier2_eclipse_sort['cumulative days'] = cum_time
tier2_eclipse_sort.drop(columns=['Unnamed: 0'])
tier2_eclipse_sort = tier2_eclipse_sort.reset_index(drop=True)
tier2_eclipse_sort.index = tier2_eclipse_sort.index + 1
print(tier2_eclipse_sort)

##### we draw the cumulative observing time

fig, ax = plt.subplots(figsize=(15, 10))

theta = 45
curve_df, fc, pc = new_cum_time(tier2_targets, theta)
ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                        alpha=1, linewidth=3, label = f'±{theta}°, full = {fc}, partial = {pc}',
                        linestyle='dashdot')

Ariel_eclipse = ax.plot(tier2_eclipse_sort.index.tolist(), tier2_eclipse_sort['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       color = 'black')

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (Tier 3 Eclipse Ranked)", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = r"Partial Observing Angle $\theta$ (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Tier2_Cul.jpg')

plt.show()
plt.close()

###################################### we look at the distribution of those targets
