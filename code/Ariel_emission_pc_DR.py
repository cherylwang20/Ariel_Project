'''
@author: Huiyi (Cheryl) Wang
August 2023

This code plots the diminishing return for observing lower signal targets at higher Tier.
Please refer to Figure 8 of Ariel_project_doc.pdf

'''

from phasecurve_plot_cheryl import *

ariel_target = pd.read_csv(os.path.join(data_dir, 'SNR_all_tier.csv'))

ariel_target = ariel_target.sort_values(by = 'Tier2_SNR',ascending=False)

############ we first do this for phase curve
ariel_target = cum_df(ariel_target)
ariel_pc_1 = cum_df_pc_N(ariel_target, Tier=1)
ariel_pc_2 = cum_df_pc_N(ariel_target, Tier=2)
ariel_pc_3 = cum_df_pc_N(ariel_target, Tier=3)
day = 2000
ariel_pc_Tier1 = ariel_pc_1[ariel_pc_1['N cumulative pc [days]'] < day]
ariel_pc_Tier2 = ariel_pc_2[ariel_pc_2['N cumulative pc [days]'] < day]

print(len(ariel_pc_2[ariel_pc_2['N cumulative pc [days]'] < 365]))
ariel_pc_Tier3 = ariel_pc_3[ariel_pc_3['N cumulative pc [days]'] < day]

fig, ax = plt.subplots(figsize=(15, 10))

Ariel_transit = ax.plot(ariel_target.index.tolist(), ariel_target['cumulative days'].tolist(),
                        alpha = 1, linewidth= 3, label = 'N = 1')

Ariel_transit_1 = ax.plot(ariel_pc_Tier1.index.tolist(), ariel_pc_Tier1['N cumulative pc [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 1')
Ariel_transit_2 = ax.plot(ariel_pc_Tier2.index.tolist(), ariel_pc_Tier2['N cumulative pc [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 2')
Ariel_transit_3 = ax.plot(ariel_pc_Tier3.index.tolist(), ariel_pc_Tier3['N cumulative pc [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 3')
plt.axhline(365, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.axhline(730, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.axhline(1095, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (Tier 2 AESM Ranked)", fontsize=22, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=22, fontweight='bold')
#plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = "Phase Curve", loc = "lower right", fontsize = 18, title_fontsize= 18)
#plt.yscale('log')
#plt.xscale('log')
plt.ylim([0,2000])
plt.savefig(save_dir+'Ariel-Phasecurves-pc_All_Tier.pdf')

plt.show()
plt.close()

############ we first do this for emission
ariel_target = cum_df_transit(ariel_target)
ariel_pc_1 = cum_df_emission_N(ariel_target, Tier=1)
ariel_pc_2 = cum_df_emission_N(ariel_target, Tier=2)
ariel_pc_3 = cum_df_emission_N(ariel_target, Tier=3)
day = 1095
ariel_pc_Tier1 = ariel_pc_1[ariel_pc_1['N cumulative emission [days]'] < day]
ariel_pc_Tier2 = ariel_pc_2[ariel_pc_2['N cumulative emission [days]'] < day]
ariel_pc_Tier3 = ariel_pc_3[ariel_pc_3['N cumulative emission [days]'] < day]

fig, ax = plt.subplots(figsize=(15, 10))

Ariel_transit = ax.plot(ariel_target.index.tolist(), ariel_target['cumulative transit [days]'].tolist(),
                        alpha = 1, linewidth= 3, label = 'N = 1')

Ariel_transit_1 = ax.plot(ariel_pc_Tier1.index.tolist(), ariel_pc_Tier1['N cumulative emission [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 1')
Ariel_transit_2 = ax.plot(ariel_pc_Tier2.index.tolist(), ariel_pc_Tier2['N cumulative emission [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 2')
Ariel_transit_3 = ax.plot(ariel_pc_Tier3.index.tolist(), ariel_pc_Tier3['N cumulative emission [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 3')
plt.axhline(365, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.axhline(730, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.axhline(1095, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (Tier 2 AESM Ranked)", fontsize=22, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=22, fontweight='bold')
#plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = "Emission Target", loc = "upper left", fontsize = 18, title_fontsize= 18)
#plt.yscale('log')
#plt.xscale('log')
#plt.ylim([0,2000])
plt.savefig(save_dir+'Ariel-emission_All_Tier.pdf')

plt.show()
plt.close()