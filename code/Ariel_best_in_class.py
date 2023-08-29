'''
@author: Huiyi (Cheryl) Wang
August 2023

This code looks at the best in class method when looking at 6/6/6/25 planets in each category
all plots contained are for bic method
'''


from phasecurve_plot_cheryl import *

ariel_cal = pd.read_csv(os.path.join(data_dir, 'SNR_all_tier.csv'))

ariel_cal = ariel_cal.sort_values(by = 'Tier1_SNR',ascending=False)
num = 6


ariel_terrestrial = ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] <= 0.16058)].head(num)
ariel_subnep = ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] >= 0.16058)
                & (ariel_cal['Planet Radius [Rj]'] <= 0.312251)].head(num)
ariel_nep = ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] <= 0.624503)
                & (ariel_cal['Planet Radius [Rj]'] >= 0.312251) ].head(num)

ariel_giant = ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] >= 0.624503)  & (ariel_cal['Tier2_SNR'] >= 7)].head(25)



ariel_4cat = pd.concat([ariel_terrestrial.head(num), ariel_subnep.head(num),
                        ariel_nep.head(num),ariel_giant.head(25) ])

print(len(ariel_4cat))

ariel_4cat = cum_df_4(ariel_4cat)


ariel_4cat.to_csv(data_dir + 'selected_target_final.csv')

angle = [45, 90]


fig, ax = plt.subplots(figsize=(15, 10))

for i in angle:
    curve_df, fc, pc = new_cum_time(ariel_4cat, i)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')

Ariel_eclipse = ax.plot(ariel_4cat.index.tolist(), ariel_4cat['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       color = 'black')

print(ariel_4cat['cumulative days'].max())

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
#plt.title("Ariel Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = r"Partial Observing Angle $\theta$ (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Tier2_allcat.pdf')

#plt.show()
plt.close()
#####################################
ariel_4cat_N = ariel_4cat.sort_values(by = 'Tier2_SNR',ascending=False)
ariel_4cat = ariel_4cat.sort_values(by = 'Tier2_SNR',ascending=False)
ariel_4cat_N = cum_df_4(ariel_4cat_N, tier = False)

fig, ax = plt.subplots(figsize=(15, 10))

for i in angle:
    curve_df, fc, pc = new_cum_time(ariel_4cat, i, False)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')
    if i == 45:
        curve_df.to_csv(data_dir + 'ariel_45.csv')

    print(i ,curve_df)
    print(i, 'average period', curve_df['Partial Period [days]'].mean() + 2*curve_df['Transit Duration [s]'].mean() / 86400)
    print(i, 'average N', curve_df['N obs'].mean())
    print(i, 'average AESM', curve_df['Tier2_SNR'].mean())

plt.axhline(365, color='black', linestyle='dashed', linewidth=2, alpha=1)

plt.axhline(365, color='black', linestyle='dashed', linewidth=2, alpha=1)

Ariel_eclipse = ax.plot(ariel_4cat_N.index.tolist(), ariel_4cat_N['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       color = 'black')
print(ariel_4cat_N['cumulative days'].max())

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
#plt.title("Ariel Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = r"Partial Observing Angle $\theta$ (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Tier2-N_allcat.pdf')

#plt.show()
plt.close()


###################################

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel_4cat['Tier2_SNR'].min(), ariel_4cat['Tier2_SNR'].max()

print(min_)
# cmap='viridis_r'
cmap = 'Spectral_r'

Ariel_terr = ax.scatter(ariel_terrestrial["Planet Period [days]"], ariel_terrestrial['pl_g'],
                        alpha=0.7, s = 50, c = ariel_terrestrial['Tier2_SNR'], cmap = cmap,
                        marker="o", linewidths = 1.5, edgecolor = 'black',
                         label = "Ariel", zorder = 1, vmin=min_, vmax=max_)

Ariel_subnep = ax.scatter(ariel_subnep["Planet Period [days]"], ariel_subnep['pl_g'],
                        alpha=0.7, s = 150, c = ariel_subnep['Tier2_SNR'], cmap = cmap,
                        marker="o", linewidths = 1.5, edgecolor = 'black',
                         label = "Ariel", zorder = 1, vmin=min_, vmax=max_)
Ariel_nep = ax.scatter(ariel_nep["Planet Period [days]"], ariel_nep['pl_g'],
                        alpha=0.7, s = 450, c = ariel_nep['Tier2_SNR'], cmap = cmap,
                        marker="o", linewidths = 1.5, edgecolor = 'black',
                         label = "Ariel", zorder = 1, vmin=min_, vmax=max_)
Ariel_giant = ax.scatter(ariel_giant["Planet Period [days]"], ariel_giant['pl_g'],
                        alpha=0.7, s = 700, c = ariel_giant['Tier2_SNR'], cmap = cmap,
                        marker="o", linewidths = 1.5, edgecolor = 'black',
                         label = "Ariel", zorder = 1, vmin=min_, vmax=max_)


clb = fig.colorbar(Ariel_terr, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Tier 2 AESM',fontsize=18)
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
plt.xscale('log')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.savefig(save_dir + 'JWST-Ariel-pg_porb_fom.pdf')

#plt.show()
plt.close()


###############################################
fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel_4cat['Planet Temperature [K]'].min(), ariel_4cat['Planet Temperature [K]'].max()
# cmap='viridis_r'
cmap = 'RdYlBu_r'

JWST_plot = ax.scatter( pc_telescope.query("JWST == 'Yes'")['pl_orbper'],pc_telescope.query("JWST == 'Yes'")["pl_radj"],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_eqt"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=1, vmin=min_, vmax=max_)

Ariel_plot = ax.scatter(ariel_4cat['Planet Period [days]'],ariel_4cat["Planet Radius [Rj]"],
                        alpha=1, s = 200, c = ariel_4cat["Planet Temperature [K]"], marker="*",
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
                   Line2D([0], [0], marker='*', color='w', label='Ariel',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25)
                   ]

first_legend = plt.legend(handles=legend_elements, loc='upper right',
                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

ax = plt.gca().add_artist(first_legend)


plt.grid(True, alpha=0.35)
plt.ylabel('Planet Radius [R$_J$]', fontsize=24, fontweight='bold')
plt.xlabel("Planet Period [days]", fontsize=28, fontweight='bold')
#plt.title("Phase Curves Targets", fontsize=28, fontweight='bold')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xscale('log')
# plt.ylim([0,105])

plt.savefig(save_dir+ 'JWST-Ariel-Phasecurves-allcat.pdf')
#plt.show()

plt.close()


############## we look at the figure for eccentricity

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = min_, max_ = ariel_4cat['Tier1 Transit S/N'].min(), ariel_4cat['Tier1 Transit S/N'].max()
# cmap='viridis_r'
cmap = 'PuOr'

#filter out eccentricities higher than 0.2
'''
ariel_terrestrial = ariel_terrestrial[ariel_terrestrial['Eccentricity'] > 0.2]
ariel_subnep = ariel_subnep[ariel_subnep['Eccentricity']> 0.2]
ariel_nep = ariel_nep[ariel_nep['Eccentricity'] > 0.2]
ariel_giant = ariel_giant[ariel_giant['Eccentricity'] > 0.2]
'''

##
Ariel_terr = ax.scatter(ariel_terrestrial["Planet Period [days]"], ariel_terrestrial['Eccentricity'],
                        alpha=0.6, s = 50, c = ariel_terrestrial["Tier1 Transit S/N"], marker="o",
                        edgecolor='black', cmap=cmap, vmin=min_, vmax=max_,
                        linewidths=1, label = "Terrestrial", zorder = 4)

Ariel_subnep = ax.scatter(ariel_subnep["Planet Period [days]"], ariel_subnep['Eccentricity'],
                        alpha=0.6, s = 150, c = ariel_subnep["Tier1 Transit S/N"], marker="o",
                        edgecolor='black', cmap=cmap, vmin=min_, vmax=max_,
                        linewidths=1, label = "SubNeptune", zorder = 3)

Ariel_nept = ax.scatter(ariel_nep["Planet Period [days]"], ariel_nep['Eccentricity'],
                        alpha=0.6, s = 400, c = ariel_nep["Tier1 Transit S/N"], marker="o",
                        edgecolor='black', cmap=cmap,vmin=min_, vmax=max_,
                        linewidths=1, label = "Neptune", zorder = 2)

Ariel_giant = ax.scatter(ariel_giant["Planet Period [days]"], ariel_giant['Eccentricity'],
                        alpha=0.6, s = 600, c = ariel_giant["Tier1 Transit S/N"], marker="o",
                        edgecolor='black', cmap=cmap, vmin=min_, vmax=max_,
                        linewidths=1, label = "Giant", zorder = 1)


# ax.set_clim(min_, max_)
clb = fig.colorbar(Ariel_terr, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
clb.set_label('Tier 1 Transmission Spectroscopy',fontsize=16)

ax.axvline(3, color='red', linestyle='dashed', linewidth=2, alpha=0.75, zorder = 0)


plt.grid(True, alpha=0.35)
plt.xlabel("Planet Period [days]", fontsize=18, fontweight='bold')
plt.ylabel("Eccentricity", fontsize=18, fontweight='bold')
#plt.title("Ariel Phase Curve Targets: Period vs Eccentricity", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.gca().set_ylim(top=1)
#plt.yscale('log')
plt.xscale('log')
#plt.ylim([0,1])
#plt.xlim([1,100])
plt.savefig(save_dir+'Ariel-Phasecurves-cat4-Ecc-Period.pdf')

#plt.show()
plt.close()


##############################now we see how much time/transit targets are also overlappinp.

cum_time = []
cum = 0
for index, row in ariel_4cat.iterrows():
    cum += row['Transit Duration [s]'] * 3 / 86400
    cum_time.append(cum)

print(f'Total Tier 2 transit time is {cum} days.')
