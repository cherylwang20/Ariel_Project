import matplotlib.pyplot as plt

from phasecurve_plot_cheryl import *

ariel_target_or = pd.read_csv(os.path.join(data_dir, 'SNR_all_tier.csv'))

ariel_target = ariel_target_or.sort_values(by = 'Tier1 Transit S/N',ascending=False)


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
plt.xlabel("# of planets (Tier 1 ATSM Ranked)", fontsize=22, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=22, fontweight='bold')
#plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = "Transit" ,loc = "upper left", fontsize = 18, title_fontsize= 18)
#plt.yscale('log')
#plt.xscale('log')
#plt.ylim([0,1095])
plt.savefig(save_dir+'Ariel-Phasecurves-Transit_All_Tier.pdf')

#plt.show()
plt.close()

###################### select targets from Tier 3 first

ariel_tier3_transit = ariel_target_3.head(60)
ariel_tier3_transit = cum_df_transit_N(ariel_tier3_transit, 3)
common_names = set(ariel_tier3_transit['Planet Name']).intersection(ariel_target['Planet Name'])

# Step 2: Drop rows with common 'name' values from both DataFrames
ariel_target = ariel_target[~ariel_target['Planet Name'].isin(common_names)]

print(len(ariel_target))

####### select target from Tier 2 list
#####
ariel_tier2_transit = cum_df_transit_N(ariel_target, Tier=2)
ariel_tier2_transit = ariel_tier2_transit[ariel_tier2_transit['N cumulative transit [days]'] < 365]

print('# of Tier 2 targets',len(ariel_tier2_transit))
common_names = set(ariel_tier2_transit['Planet Name']).intersection(ariel_target['Planet Name'])

# Step 2: Drop rows with common 'name' values from both DataFrames
ariel_target = ariel_target[~ariel_target['Planet Name'].isin(common_names)]

print(len(ariel_target))
ariel_tier1_transit = cum_df_transit_N(ariel_target, Tier=1)

ariel_tier1_transit = ariel_tier1_transit[ariel_tier1_transit['N cumulative transit [days]'] < 600]

print('# of Tier 1 targets', len(ariel_tier1_transit))
fig, ax = plt.subplots(figsize=(15, 10))

tier_1_index = [x + len(ariel_tier2_transit) + len(ariel_tier3_transit) for x in ariel_tier1_transit.index.tolist()]
tier_1_list = [x  + ariel_tier2_transit['N cumulative transit [days]'].max()+ ariel_tier3_transit['N cumulative transit [days]'].max() for x in ariel_tier1_transit['N cumulative transit [days]'].tolist()]


Ariel_transit_1= ax.plot(tier_1_index,tier_1_list, color = 'blue',
                          alpha = 1, linewidth= 5)
dashed_1_list = [x - 69 + ariel_tier2_transit['N cumulative transit [days]'].max()+ ariel_tier3_transit['N cumulative transit [days]'].max() for x in ariel_transit_365_Tier1['N cumulative transit [days]'].tolist()]

Ariel_transit_1 = ax.plot(ariel_transit_365_Tier1.index.tolist(), dashed_1_list,
                          color = 'blue', linestyle = 'dashed',
                          alpha = 1, linewidth= 3)


tier_2_index = [x + len(ariel_tier3_transit) for x in ariel_tier2_transit.index.tolist()]
tier_2_list = [x  + ariel_tier3_transit['N cumulative transit [days]'].max() for x in ariel_tier2_transit['N cumulative transit [days]'].tolist()]

dashed_2_index = [x + len(ariel_tier3_transit) for x in ariel_transit_365_Tier2.index.tolist()]
dashed_2_list = [x  + ariel_tier3_transit['N cumulative transit [days]'].max() - 75 for x in ariel_transit_365_Tier2['N cumulative transit [days]'].tolist()]

Ariel_transit_2 = ax.plot(ariel_transit_365_Tier2.index.tolist(), dashed_2_list,
                          alpha = 1, linewidth= 3,color = 'orange', linestyle = 'dashed')

Ariel_transit_2 = ax.plot(tier_2_index, tier_2_list, color = 'orange',
                          alpha = 1, linewidth= 5)







Ariel_transit_3 = ax.plot(ariel_transit_365_Tier3.index.tolist(), ariel_transit_365_Tier3['N cumulative transit [days]'].tolist(),
                          alpha = 1, linewidth= 3,  color = 'green', linestyle = 'dashed')
Ariel_transit_3 = ax.plot(ariel_tier3_transit.index.tolist(), ariel_tier3_transit['N cumulative transit [days]'].tolist(),
                          alpha = 1, linewidth= 5,  color = 'green')

plt.axhline(365, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.axhline(730, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.axhline(1095, color='black', linestyle='dashed', linewidth=2, alpha=1)
plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (Tier 1 ATSM Ranked)", fontsize=22, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=22, fontweight='bold')
#plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
from matplotlib.lines import Line2D
line1 = Line2D([0], [0], label='Tier 1', color='blue', linewidth= 5)
line2 = Line2D([0], [0], label='Tier 2', color='orange', linewidth= 5)
line3 = Line2D([0], [0], label='Tier 3', color='green', linewidth= 5)

# access legend objects automatically created from data
handles, labels = plt.gca().get_legend_handles_labels()
handles.extend([line1, line2, line3])

plt.legend(handles=handles, fontsize = 20, loc = 'lower right')
#plt.yscale('log')
#plt.xscale('log')
plt.ylim([0,1095])
plt.savefig(save_dir+'Ariel-Transit_All_Tier.pdf')

plt.show()
plt.close()

################# create scattered plot for each
fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel_target_or['Planet Temperature [K]'].min(), ariel_target_or['Planet Temperature [K]'].max()
# cmap='viridis_r'
cmap = 'RdYlBu_r'

'''
JWST_plot = ax.scatter( pc_telescope.query("JWST == 'Yes'")['pl_orbper'],pc_telescope.query("JWST == 'Yes'")["pl_radj"],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_eqt"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=1, vmin=min_, vmax=max_)
'''
Ariel_plot = ax.scatter(ariel_tier1_transit['Planet Period [days]'],ariel_tier1_transit["Planet Radius [Rj]"],
                        alpha=0.7, s = 200, c = ariel_tier1_transit["Planet Temperature [K]"], marker="o",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 2, vmin=min_, vmax=max_)
Ariel_plot = ax.scatter(ariel_tier2_transit['Planet Period [days]'],ariel_tier2_transit["Planet Radius [Rj]"],
                        alpha=0.7, s = 200, c = ariel_tier2_transit["Planet Temperature [K]"], marker="*",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 2, vmin=min_, vmax=max_)
Ariel_plot = ax.scatter(ariel_tier3_transit['Planet Period [days]'],ariel_tier3_transit["Planet Radius [Rj]"],
                        alpha=0.7, s = 200, c = ariel_tier3_transit["Planet Temperature [K]"], marker="^",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 2, vmin=min_, vmax=max_)

clb = fig.colorbar(Ariel_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planetary Equilibrium Temperature [K]',fontsize=18)
clb.ax.tick_params(labelsize=17)

ax.axhline(0.160586, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axhline(0.312251, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axhline(0.624503, color='g', linestyle='dashed', linewidth=1, alpha=1)


from matplotlib.lines import Line2D

legend_elements = [#Line2D([0], [0], marker='h', color='w', label='JWST',
                         # markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                   Line2D([0], [0], marker='o', color='w', label='Tier 1',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                    Line2D([0], [0], marker='*', color='w', label='Tier 2',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                    Line2D([0], [0], marker='^', color='w', label='Tier 3',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25)
                   ]

first_legend = plt.legend(handles=legend_elements, loc='upper right',
                          title="$\\bf{Transit \quad Tier} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

ax = plt.gca().add_artist(first_legend)


plt.grid(True, alpha=0.35)
plt.ylabel('Planet Radius [R$_J$]', fontsize=24, fontweight='bold')
plt.xlabel("Planet Period [days]", fontsize=24, fontweight='bold')
#plt.title("Phase Curves Targets", fontsize=28, fontweight='bold')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xscale('log')
# plt.ylim([0,105])

plt.savefig(save_dir+ 'JWST-Ariel-transit_all_tier.pdf')
#plt.show()

plt.close()

############## create a histogram for those different tiers


transit_1 = ariel_tier1_transit['Transit Duration [s]']/3600
ATSM_1 = ariel_tier1_transit['Tier1 Transit S/N']

transit_2 = ariel_tier2_transit['Transit Duration [s]']/3600
ATSM_2 = ariel_tier2_transit['Tier2 Transit S/N']

transit_3= ariel_tier3_transit['Transit Duration [s]']/3600
ATSM_3 = ariel_tier3_transit['Tier3 Transit S/N']

bin_num = 10

fig, (ax1, ax2) = plt.subplots(1, 2, sharey= True, figsize=(15, 10))
ax1.set_xlabel("Transit Duration [hours]", fontsize=20, fontweight='bold')
ax1.set_ylabel("# of planets", fontsize=20, fontweight='bold')
ax1.tick_params(axis="x", labelsize=17)
ax1.tick_params(axis="y", labelsize=17)
#ax1.set_xlim(xmin=0, xmax = 26)
ax1.hist([transit_1, transit_2, transit_3], bins= bin_num, rwidth= 1,
         label = ['Tier 1', 'Tier 2', 'Tier 3'], color = ['green', 'lime', 'greenyellow'])
ax1.legend(fontsize = 18)



plt.xlabel("ATSM", fontsize=20, fontweight='bold')
plt.ylabel("# of planets", fontsize=20, fontweight='bold')
#plt.title("Histogram of 42 selected targets", fontsize=24, fontweight='bold')

plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
ax2.hist([ATSM_1,ATSM_2,ATSM_3], bins = bin_num, rwidth=1,
         label = ['Tier 1', 'Tier 2', 'Tier 3'], color= ['maroon', 'salmon', 'orange'])
#fig.suptitle("Histogram of 42 selected targets", fontsize=24, fontweight='bold')
plt.legend(fontsize = 18)
plt.savefig(save_dir + 'Ariel_histogram_transit.pdf')

plt.show()
plt.close()


#################### sky map

phase_curve_target = pd.read_csv(os.path.join(data_dir, 'Tier_2_emission.csv'))

phase_curve_target['Star RA'] = np.deg2rad(phase_curve_target['Star RA'])
phase_curve_target['Star RA'] = np.mod(phase_curve_target['Star RA'] + np.pi, 2*np.pi) - np.pi

print(phase_curve_target['Star RA'])

ariel_tier1_transit['Star RA'] = np.deg2rad(ariel_tier1_transit['Star RA'])
ariel_tier1_transit['Star RA'] = np.mod(ariel_tier1_transit['Star RA'] + np.pi, 2*np.pi) - np.pi

ariel_tier2_transit['Star RA'] = np.deg2rad(ariel_tier2_transit['Star RA'])
ariel_tier2_transit['Star RA'] = np.mod(ariel_tier2_transit['Star RA'] + np.pi, 2*np.pi) - np.pi

ariel_tier3_transit['Star RA'] = np.deg2rad(ariel_tier3_transit['Star RA'])
ariel_tier3_transit['Star RA'] = np.mod(ariel_tier3_transit['Star RA'] + np.pi, 2*np.pi) - np.pi


fig = plt.figure(figsize=(12, 8))

# Apply the aitoff projection and activate the grid
ax = plt.subplot(111, projection="aitoff")
plt.grid(True)

ax.scatter(ariel_tier1_transit['Star RA'], ariel_tier1_transit['Star Dec']*np.pi/180, color = 'blue', s = 120, label = 'Tier 1 Transit')
ax.scatter(ariel_tier2_transit['Star RA'], ariel_tier2_transit['Star Dec']*np.pi/180, color = 'yellow', s = 120, label = 'Tier 2 Transit')
ax.scatter(ariel_tier3_transit['Star RA'], ariel_tier3_transit['Star Dec']*np.pi/180, color = 'lime', s = 120, label = 'Tier 3 Transit')


ax.scatter(phase_curve_target['Star RA'], phase_curve_target['Star Dec']*np.pi/180, color = 'red', s = 130,
           edgecolor = 'black', marker='h', label = 'Phase Curve')

# Set long. / lat. labels
#plt.xlabel('Long. in deg', fontsize=20, fontweight='bold')
#plt.ylabel('Lat. in deg',fontsize=20, fontweight='bold')
plt.legend(fontsize = 12)

# Save the figure
plt.savefig(save_dir + 'Ariel_skymap_all.pdf', dpi=300)
plt.show()