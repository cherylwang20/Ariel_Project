'''
@author: Huiyi (Cheryl) Wang
August 2023

This code provides comparsion between Best in class and Ranked FoM method
which is section 3.3 in Ariel_project_doc.pdf, Figure 21 - 23
'''

from Tier_2_target_analysis import *
from Ariel_best_in_class import *


period = target_45['Planet Period [days]']
N_obs_rfm = target_45['N obs']
N_obs_bic = ariel_4cat['N obs']
#transit = target_45['Transit Duration [s]']
AESM_rfm = target_45['Tier2_SNR']
AESM_bic = ariel_4cat['Tier2_SNR']

print(AESM.min())

bins = 15
fig, (ax1, ax2) = plt.subplots(1, 2, sharey= True, figsize=(15, 10))
ax1.set_xlabel(r"$N_{obs}$", fontsize=24, fontweight='bold')
ax1.set_ylabel("# of planets", fontsize=24, fontweight='bold')
ax1.tick_params(axis="x", labelsize=17)
ax1.tick_params(axis="y", labelsize=17)
ax1.set_xscale('log')
his, bin = np.histogram(N_obs_bic, bins=bins)
logbin = np.logspace(np.log10(bin[0]),np.log10(bin[-1]),len(bin))
ax1.hist([N_obs_rfm, N_obs_bic], bins= logbin, rwidth=3,
         color = ['deepskyblue', 'orange'], label= ['Ranked FoM', 'Best in Class'])
ax1.legend(prop={'size': 18})



plt.xlabel("Tier 2 AESM", fontsize=24, fontweight='bold')
plt.ylabel("# of planets", fontsize=24, fontweight='bold')
#plt.title("Histogram of 42 selected targets", fontsize=24, fontweight='bold')


hist, bins = np.histogram(AESM_bic, bins=bins)
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
ax2.hist([AESM_rfm, AESM_bic], bins = logbins, rwidth= 0.85,
         color = ['deepskyblue', 'orange'], label= ['Ranked FoM', 'Best in Class'])
#fig.suptitle("Histogram of 42 selected targets", fontsize=24, fontweight='bold')
plt.xscale('log')
ax2.legend(prop={'size': 18})
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.savefig(save_dir + 'Ariel_histogram_compare.pdf')

plt.show()
plt.close()

######################################
# here we compare the two required time for observations.

fig, ax = plt.subplots(figsize=(15, 10))

theta = [45, 90]

for i in theta:
    curve_df, fc, pc = new_cum_time(Tier_2_target, i, False)
    rfm = ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')

tier2_SNR_sort = cum_df_4(Tier_2_target, False)
tier2_SNR_sort = tier2_SNR_sort[tier2_SNR_sort['cumulative days'] < 365]
print(len(tier2_SNR_sort))
Ariel_eclipse_rfm = ax.plot(tier2_SNR_sort.index.tolist(), tier2_SNR_sort['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                        color = 'black', linestyle='dashdot')
color = ['#1f77b4', '#ff7f0e' ]
j = 0
for i in angle:
    curve_df, fc, pc = new_cum_time(ariel_4cat, i, False)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dotted', color = color[j])
    j += 1


plt.axhline(365, color='green', linestyle='dashed', linewidth=2, alpha=1)


Ariel_eclipse = ax.plot(ariel_4cat_N.index.tolist(), ariel_4cat_N['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       linestyle = 'dotted', color = 'black')

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (Tier 2 AESM Ranked)", fontsize=22, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=22, fontweight='bold')
#plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)


from matplotlib.lines import Line2D


custom_style = [Line2D([0], [0], color='black', lw=4, linestyle= 'dotted', label = 'Best in Class'),
                Line2D([0], [0], color='black', lw=4, linestyle= 'dashdot', label = 'Ranked FoM')]


first_legend = plt.legend(handles=custom_style, loc='upper left', title_fontsize=20, prop={'size': 20})

plt.gca().add_artist(first_legend)
custom_lines = [Line2D([0], [0], color='#1f77b4', lw=4),
                Line2D([0], [0], color='#ff7f0e', lw=4),
                Line2D([0], [0], color='black', lw=4)]

ax.legend(custom_lines, ['Full Phase Curve', '±45°', '±90°'], title = r"Partial Observing Angle $\theta$ (°)",
          title_fontsize=20, prop={'size': 20}, loc = 'lower right')

#plt.legend(title = r"Partial Observing Angle $\theta$ (°)", loc = "upper right", fontsize = 15, title_fontsize= 15)
plt.yscale('log')
plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Tier2_Cul_compare.pdf')

plt.show()
plt.close()

################################################
# first, we create a histogram of the targets when we only observe once

from Ariel_bic_365 import *

ariel_target = pd.read_csv(os.path.join(data_dir, 'SNR_all_tier.csv'))
ariel_target = ariel_target.sort_values(by = 'Tier2_SNR',ascending=False)
ariel_rfm_n1 = new_cum_time(ariel_target,45)[0]


period_n1_bic = ariel_4cat_45['Planet Period [days]']
aesm_n1_bic = ariel_4cat_45['Tier2_SNR']

period_n1_rfm = ariel_rfm_n1['Planet Period [days]']
aesm_n1_rfm = ariel_rfm_n1['Tier2_SNR']

bins = 15
fig, (ax1, ax2) = plt.subplots(1, 2, sharey= True, figsize=(15, 10))
ax1.set_xlabel('Planet Period [days]', fontsize=24, fontweight='bold')
ax1.set_ylabel("# of planets", fontsize=24, fontweight='bold')
ax1.tick_params(axis="x", labelsize=17)
ax1.tick_params(axis="y", labelsize=17)
ax1.set_xscale('log')
his, bin = np.histogram(period_n1_bic, bins=bins)
logbin = np.logspace(np.log10(bin[0]),np.log10(bin[-1]),len(bin))
ax1.hist([aesm_n1_rfm, period_n1_bic], bins= logbin, rwidth=3,
         color = ['deepskyblue', 'orange'], label= ['Ranked FoM', 'Best in Class'])
ax1.legend(prop={'size': 18})



plt.xlabel("Tier 2 AESM", fontsize=24, fontweight='bold')
plt.ylabel("# of planets", fontsize=24, fontweight='bold')
#plt.title("Histogram of 42 selected targets", fontsize=24, fontweight='bold')


hist, bins = np.histogram(aesm_n1_bic, bins=bins)
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
ax2.hist([period_n1_rfm, aesm_n1_bic], bins = logbins, rwidth= 0.85,
         color = ['deepskyblue', 'orange'], label= ['Ranked FoM', 'Best in Class'])
#fig.suptitle("Histogram of 42 selected targets", fontsize=24, fontweight='bold')
plt.xscale('log')
ax2.legend(prop={'size': 18})
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.savefig(save_dir + 'Ariel_histogram_compare_N1.pdf')

plt.show()
plt.close()