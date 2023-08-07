from phasecurve_plot_cheryl import *

ariel_target = pd.read_csv(os.path.join(data_dir, 'SNR_all_1.csv'))

ariel_target = ariel_target.sort_values(by = 'Tier1 Transit S/N',ascending=False)

ariel_transit = ariel_target[ariel_target['Tier1 Transit S/N'] > 10]

print(len(ariel_transit))

#################

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel_transit['Planet Temperature [K]'].min(), ariel_transit['Planet Temperature [K]'].max()
# cmap='viridis_r'
cmap = 'RdYlBu_r'

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")['pl_orbper'],pc_telescope.query("JWST == 'Yes'")["pl_radj"],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_eqt"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=1, vmin=min_, vmax=max_)

Ariel_plot = ax.scatter( ariel_transit['Planet Period [days]'],ariel_transit["Planet Radius [Rj]"],
                        alpha=1, s = 200, c = ariel_transit["Planet Temperature [K]"], marker="*",
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
                   Line2D([0], [0], marker='*', color='w', label='Ariel Tier 1 ATSM > 10',
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
plt.savefig(save_dir+ 'JWST-Ariel-Phasecurves-Tier_1-Trans.pdf')

plt.show()
plt.close()


################ transit histogram

radius = ariel_transit['Planet Radius [Rj]']
transit = ariel_transit['Transit Duration [s]']


fig, (ax1, ax2) = plt.subplots(1, 2, sharey= True, figsize=(18, 10))
ax1.set_xlabel("Planet Radius [Rj]", fontsize=20, fontweight='bold')
ax1.set_ylabel("# of planets", fontsize=20, fontweight='bold')
ax1.tick_params(axis="x", labelsize=17)
ax1.tick_params(axis="y", labelsize=17)
#ax1.set_xlim(xmin=0, xmax = 26)
ax1.hist(radius, bins= 'auto', rwidth= 0.85, color = 'green')


plt.xlabel("Transit Duration [hrs]", fontsize=20, fontweight='bold')
plt.ylabel("# of planets", fontsize=20, fontweight='bold')
#plt.title("Histogram of 42 selected targets", fontsize=24, fontweight='bold')

plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
ax2.hist(transit*3/3600, bins = 'auto', rwidth= 0.85, color= 'red')
#fig.suptitle("Histogram of 42 selected targets", fontsize=24, fontweight='bold')

plt.savefig(save_dir + 'Ariel_histogram_transit.pdf')

plt.show()

##################################
Tier_2_target= pd.read_csv(os.path.join(data_dir, 'SNR_all_2.csv'))

Tier_2_emission = Tier_2_target[Tier_2_target['Tier2_SNR'] > 7]


df = Tier_2_emission[Tier_2_emission["Planet Name"].isin(ariel_transit["Planet Name"])]


cum_time = []
cum = 0
for index, row in df.iterrows():
    cum += row['Transit Duration [s]'] * 3 / 86400
    cum_time.append(cum)

print(f'Total Tier 2 transit time is {cum} days.')


print(df)

target_45 = new_cum_time(Tier_2_target, 45, False)[0]

df2 = target_45[target_45["Planet Name"].isin(ariel_transit["Planet Name"])]

print(df2)

cum_time = []
cum = 0
for index, row in df2.iterrows():
    cum += row['Transit Duration [s]'] * 3 / 86400
    cum_time.append(cum)

print(f'Total Tier 2 transit time is {cum} days.')
