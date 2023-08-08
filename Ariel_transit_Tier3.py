from phasecurve_plot_cheryl import *

ariel_target = pd.read_csv(os.path.join(data_dir, 'SNR_all_tier.csv'))

ariel_target = ariel_target.sort_values(by = 'Tier1 Transit S/N',ascending=False)


################

ariel_target = cum_df_transit(ariel_target)
ariel_target_1 = cum_df_transit_N(ariel_target, Tier=1)
ariel_target_2 = cum_df_transit_N(ariel_target, Tier=2)
ariel_target_3 = cum_df_transit_N(ariel_target, Tier=3)


ariel_transit_365_Tier1 = ariel_target_1[ariel_target_1['N cumulative transit [days]'] < 1095]
ariel_transit_365_Tier2 = ariel_target_2[ariel_target_2['N cumulative transit [days]'] < 1095]
ariel_transit_365_Tier3 = ariel_target_3[ariel_target_3['N cumulative transit [days]'] < 1095]
print(len(ariel_transit_365_Tier3))
ariel_transit_365_Tier3.to_csv(data_dir + 'ariel_transit_Tier3_365.csv')

fig, ax = plt.subplots(figsize=(15, 10))

Ariel_transit = ax.plot(ariel_target.index.tolist(), ariel_target['cumulative transit [days]'].tolist(),
                        alpha = 1, linewidth= 3, label = 'N = 1')

Ariel_transit_1 = ax.plot(ariel_transit_365_Tier1.index.tolist(), ariel_transit_365_Tier1['N cumulative transit [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 1')
Ariel_transit_2 = ax.plot(ariel_transit_365_Tier2.index.tolist(), ariel_transit_365_Tier2['N cumulative transit [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 2')
Ariel_transit_3 = ax.plot(ariel_transit_365_Tier3.index.tolist(), ariel_transit_365_Tier3['N cumulative transit [days]'].tolist(),
                          alpha = 1, linewidth= 3, label = 'Tier 3')
plt.axhline(365, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.axhline(730, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.axhline(1095, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (Tier 1 ATSM Ranked)", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
#plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
#plt.ylim([0,1095])
plt.savefig(save_dir+'Ariel-Phasecurves-Transit_All_Tier.pdf')

plt.show()
plt.close()

###################### select targets from Tier 3 first

ariel_tier3_transit = ariel_target_3.head(60)
common_names = set(ariel_tier3_transit['Planet Name']).intersection(ariel_target['Planet Name'])

# Step 2: Drop rows with common 'name' values from both DataFrames
ariel_target = ariel_target[~ariel_target['Planet Name'].isin(common_names)]

print(len(ariel_target))