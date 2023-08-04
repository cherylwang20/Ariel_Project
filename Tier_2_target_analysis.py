from phasecurve_plot_cheryl import *

###### we look at the 51 Tier 2 emission spectroscopy targets calculate by Ariel_tiers_calculation.py

Tier_2_target= pd.read_csv(os.path.join(data_dir, 'SNR_all_2.csv'))

Tier_2_emission = Tier_2_target[Tier_2_target['Tier2_SNR'] > 7]
Tier_2_emission.to_csv(data_dir + 'Tier_2_emission.csv')


################calculate total overlapping transit time
tier_2_trans = [0, 2, 4, 5, 18, 36, 51, 58, 206, 326, 350]
tier_2_trans = ariel.iloc[tier_2_trans]

cum_time = []
cum = 0
for index, row in tier_2_trans.iterrows():
    cum += row['Transit Duration [s]'] * 3 / 86400
    cum_time.append(cum)

print(f'Total Tier 2 transit time is {cum} days.')

##########################33


tier2_SNR_sort = Tier_2_emission.sort_values(by = 'Tier2_SNR',ascending=False)
cum_time = []
cum = 0
for index, row in tier2_SNR_sort.iterrows():
    cum += row['Planet Period [days]'] + 2*row['Transit Duration [s]']/ 86400
    cum_time.append(cum)

tier2_SNR_sort['cumulative days'] = cum_time
tier2_SNR_sort.drop(columns=['Unnamed: 0'])
tier2_SNR_sort = tier2_SNR_sort.reset_index(drop=True)
tier2_SNR_sort.index = tier2_SNR_sort.index + 1
#print(tier2_SNR_sort)

##### we draw the cumulative observing time

fig, ax = plt.subplots(figsize=(15, 10))

theta = [45, 90]

for i in theta:
    curve_df, fc, pc = new_cum_time(tier2_SNR_sort, i)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')

Ariel_eclipse = ax.plot(tier2_SNR_sort.index.tolist(), tier2_SNR_sort['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                        color = 'black')

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (Tier 3 Eclipse Ranked)", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
#plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = r"Partial Observing Angle $\theta$ (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Tier2_Cul.pdf')

plt.show()
plt.close()

###################################### we look at the distribution of those targets

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = tier2_SNR_sort['Planet Temperature [K]'].min(), tier2_SNR_sort['Planet Temperature [K]'].max()
# cmap='viridis_r'
cmap = 'RdYlBu_r'

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")['pl_orbper'],pc_telescope.query("JWST == 'Yes'")["pl_radj"],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_eqt"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=1, vmin=min_, vmax=max_)

Ariel_plot = ax.scatter( tier2_SNR_sort['Planet Period [days]'],tier2_SNR_sort["Planet Radius [Rj]"],
                        alpha=1, s = 200, c = tier2_SNR_sort["Planet Temperature [K]"], marker="*",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 2, vmin=min_, vmax=max_)

clb = fig.colorbar(JWST_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planetary Equilibrium Temperature [K]',fontsize=18)
clb.ax.tick_params(labelsize=17)

ax.axhline(0.160586, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axhline(0.312251, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axhline(0.624503, color='g', linestyle='dashed', linewidth=1, alpha=1)


from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='h', color='w', label='JWST',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                   Line2D([0], [0], marker='*', color='w', label='Ariel Tier 2',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25)
                   ]

first_legend = plt.legend(handles=legend_elements, loc='upper right',
                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

ax = plt.gca().add_artist(first_legend)


plt.grid(True, alpha=0.35)
plt.ylabel('Planet Radius [R$_J$]', fontsize=24, fontweight='bold')
plt.xlabel("Planet Period [days]", fontsize=24, fontweight='bold')
#plt.title("Phase Curves Targets", fontsize=28, fontweight='bold')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+ 'JWST-Ariel-Phasecurves-Tier_2.pdf')

plt.show()
plt.close()

############ calculate how many of those overlap with the transit targets.

####################################################3

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = tier2_SNR_sort['Tier2_SNR'].min(), tier2_SNR_sort['Tier2_SNR'].max()

print(min_)
# cmap='viridis_r'
cmap = 'Spectral_r'


Ariel_plot = ax.scatter(tier2_SNR_sort["Planet Period [days]"], tier2_SNR_sort['pl_g'],
                        alpha=0.7, s = 700, c = tier2_SNR_sort["Tier2_SNR"], marker="o",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 1, vmin=min_, vmax=max_)



clb = fig.colorbar(Ariel_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Tier 2 Emission Figure of Merit (FoM)',fontsize=18)
clb.ax.tick_params(labelsize=17)
################################################################################3


# Create another legend for the second line.
#plt.legend(handles=[eccen_plot], loc='lower right',
#           title="$\\bf{Eccentric \ Planets}$", title_fontsize=15, prop={'size': 15}, fancybox=True)

plt.grid(True, alpha=0.35)
plt.ylabel(r"Planet Gravity [$m/s^2$]", fontsize=24, fontweight = 'bold')
plt.xlabel("Planet Period [days]", fontsize=24 , fontweight = 'bold')
#plt.title("Planets Observed with Phase Curves", fontsize=24 , fontweight = 'bold')
plt.yscale('log')
#plt.xscale('log')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.savefig(save_dir + 'Ariel-51_fom.pdf')

plt.show()
plt.close()

#################### four time cumulative

fig, ax = plt.subplots(figsize=(15, 10))

theta = [45, 90]

for i in theta:
    curve_df, fc, pc = new_cum_time(Tier_2_target, i, False)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')
tier2_SNR_sort = cum_df_4(Tier_2_target, False)
tier2_SNR_sort = tier2_SNR_sort[tier2_SNR_sort['cumulative days'] < 365]
print(len(tier2_SNR_sort))
Ariel_eclipse = ax.plot(tier2_SNR_sort.index.tolist(), tier2_SNR_sort['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                        color = 'black')

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets (AESM Eclipse Ranked)", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
#plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = r"Partial Observing Angle $\theta$ (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Tier2_Cul_N4.pdf')

plt.show()
plt.close()

############ 45 phase curve targets

target_45 = new_cum_time(Tier_2_target, 45, False)[0]

print(target_45['Tier2_SNR'].min())

period = target_45['Planet Period [days]']
transit = target_45['Transit Duration [s]']


fig, (ax1, ax2) = plt.subplots(1, 2, sharey= True, figsize=(18, 10))
ax1.set_xlabel("Planet Period [days]", fontsize=20, fontweight='bold')
ax1.set_ylabel("# of planets", fontsize=20, fontweight='bold')
ax1.tick_params(axis="x", labelsize=17)
ax1.tick_params(axis="y", labelsize=17)
ax1.set_xlim(xmin=0, xmax = 26)
ax1.hist(period, bins= 'auto', rwidth= 0.85, color = 'green')


plt.xlabel("Transit Duration [hrs]", fontsize=20, fontweight='bold')
plt.ylabel("# of planets", fontsize=20, fontweight='bold')
#plt.title("Histogram of 42 selected targets", fontsize=24, fontweight='bold')

plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
ax2.hist(transit*3/3600, bins = 'auto', rwidth= 0.85, color= 'red')
#fig.suptitle("Histogram of 42 selected targets", fontsize=24, fontweight='bold')

plt.savefig(save_dir + 'Ariel_histogram_365d.pdf')

plt.show()

###################################### we look at the distribution of those targets

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = tier2_SNR_sort['Planet Temperature [K]'].min(), tier2_SNR_sort['Planet Temperature [K]'].max()
# cmap='viridis_r'
cmap = 'RdYlBu_r'

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")['pl_orbper'],pc_telescope.query("JWST == 'Yes'")["pl_radj"],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_eqt"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=1, vmin=min_, vmax=max_)

Ariel_plot = ax.scatter( tier2_SNR_sort['Planet Period [days]'],tier2_SNR_sort["Planet Radius [Rj]"],
                        alpha=1, s = 200, c = tier2_SNR_sort["Planet Temperature [K]"], marker="*",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 2, vmin=min_, vmax=max_)

clb = fig.colorbar(JWST_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planetary Equilibrium Temperature [K]',fontsize=18)
clb.ax.tick_params(labelsize=17)

ax.axhline(0.160586, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axhline(0.312251, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axhline(0.624503, color='g', linestyle='dashed', linewidth=1, alpha=1)


from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='h', color='w', label='JWST',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                   Line2D([0], [0], marker='*', color='w', label='Ariel Tier 2',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25)
                   ]

first_legend = plt.legend(handles=legend_elements, loc='upper right',
                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

ax = plt.gca().add_artist(first_legend)


plt.grid(True, alpha=0.35)
plt.ylabel('Planet Radius [R$_J$]', fontsize=24, fontweight='bold')
plt.xlabel("Planet Period [days]", fontsize=24, fontweight='bold')
#plt.title("Phase Curves Targets", fontsize=28, fontweight='bold')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+ 'JWST-Ariel-Phasecurves-Tier_2.pdf')

plt.show()
plt.close()