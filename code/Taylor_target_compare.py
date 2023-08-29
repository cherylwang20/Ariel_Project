'''
@author: Huiyi (Cheryl) Wang
August 2023

This code plots the day and night time ESM of the 16 targets in Taylor's paper on Spitzer reanalysis.

This section is not included in the Ariel_project_doc.pdf
'''


from phasecurve_plot_cheryl import *
from backup_code import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = selected_sample['T night (K)'].min(), selected_sample['T day (K)'].max()

cmap = 'RdYlBu_r'
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
print(selected_sample[selected_sample['Planet Name'] == 'HAT-P-7 b'])
print(selected_sample[selected_sample['Planet Name'] == 'HD 189733 b'])

Ariel_target_ESM_Day = ax.scatter(selected_sample['Planet Name'], selected_sample['ESM High'],
                                    alpha=1, s=250, c=selected_sample['T day (K)'], marker="o", edgecolor='black',
                                    label="Day side", zorder=2, cmap = cmap, vmin=min_, vmax=max_
                                    )


Ariel_target_ESM_Night = ax.scatter(selected_sample['Planet Name'], selected_sample['ESM Low'],
                                    alpha=1, s=250, c=selected_sample['T night (K)'], marker="*", edgecolor='black',
                                    label="Night Side", zorder=2, cmap = cmap, vmin=min_, vmax=max_
                                    )
plt.xticks(rotation=45)

clb = fig.colorbar(Ariel_target_ESM_Day, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Temperature (K)',fontsize=16)

from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Day Side',
                          markerfacecolor='none', markeredgecolor='black', mew=1, markersize=10),
                   Line2D([0], [0], marker='*', color='w', label='Night Side',
                          markerfacecolor='none', markeredgecolor='black', mew=1, markersize=10)
                   ]

first_legend = plt.legend(handles=legend_elements, loc='lower right',
                           prop={'size': 10}, fancybox=True)


plt.grid(True, alpha=0.35)
plt.xlabel("Planet Name", fontsize=18)
plt.ylabel("Emission Spectroscopy Metric (ESM)", fontsize=18)
plt.title("Ariel Phase Curve Targets: Day vs Night side ESM", fontsize=24)
plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-PhaseCurve-Day-Night-ESM.jpg')

plt.show()