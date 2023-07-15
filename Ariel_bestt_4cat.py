from phasecurve_plot_cheryl import *

ariel_cal = pd.read_csv(os.path.join(data_dir, 'SNR_all.csv'))

ariel_cal = ariel_cal.sort_values(by = 'Tier_SNR',ascending=False)

print(ariel_cal.head())
num = 10


ariel_terrestrial = ariel_cal.loc[ariel_cal['Planet Radius [Rj]'] <= 0.16058].head(num)
ariel_subnep = ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] >= 0.16058)
                & (ariel_cal['Planet Radius [Rj]'] <= 0.312251)].head(num)
ariel_nep = ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] <= 0.624503)
                & (ariel_cal['Planet Radius [Rj]'] >= 0.312251)].head(num)
ariel_giant = ariel_cal.loc[ariel_cal['Planet Radius [Rj]'] >= 0.624503].head(20)

print(ariel_terrestrial.head())


ariel_4cat = pd.concat([ariel_terrestrial.head(num), ariel_subnep.head(num),
                        ariel_nep.head(num), ariel_giant.head(20)])

angle = [45, 90]

ariel_4cat = cum_df(ariel_4cat)

fig, ax = plt.subplots(figsize=(15, 10))

for i in angle:
    curve_df, fc, pc = new_cum_time(ariel_4cat, i)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')

Ariel_eclipse = ax.plot(ariel_4cat.index.tolist(), ariel_4cat['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       color = 'black')

plt.grid(True, alpha=0.35)
plt.xlabel("# of planets", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
plt.title("Ariel Tier 2 Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = r"Partial Observing Angle $\theta$ (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Tier2_allcat.jpg')

plt.show()
plt.close()


###################################

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel_4cat['Tier_SNR'].min(), ariel_4cat['Tier_SNR'].max()
# cmap='viridis_r'
cmap = 'Spectral_r'

Ariel_terr = ax.scatter(ariel_terrestrial["Planet Period [days]"], ariel_terrestrial['pl_g'],
                        alpha=0.7, s = 50, c = ariel_terrestrial['Tier_SNR'], cmap = cmap,
                        marker="o", linewidths = 1.5, edgecolor = 'black',
                         label = "Ariel", zorder = 1, vmin=min_, vmax=max_)

Ariel_subnep = ax.scatter(ariel_subnep["Planet Period [days]"], ariel_subnep['pl_g'],
                        alpha=0.7, s = 150, c = ariel_subnep['Tier_SNR'], cmap = cmap,
                        marker="o", linewidths = 1.5, edgecolor = 'black',
                         label = "Ariel", zorder = 1, vmin=min_, vmax=max_)
Ariel_nep = ax.scatter(ariel_nep["Planet Period [days]"], ariel_nep['pl_g'],
                        alpha=0.7, s = 450, c = ariel_nep['Tier_SNR'], cmap = cmap,
                        marker="o", linewidths = 1.5, edgecolor = 'black',
                         label = "Ariel", zorder = 1, vmin=min_, vmax=max_)
Ariel_giant = ax.scatter(ariel_giant["Planet Period [days]"], ariel_giant['pl_g'],
                        alpha=0.7, s = 700, c = ariel_giant['Tier_SNR'], cmap = cmap,
                        marker="o", linewidths = 1.5, edgecolor = 'black',
                         label = "Ariel", zorder = 1, vmin=min_, vmax=max_)


clb = fig.colorbar(Ariel_terr, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Figure of Merit (FoM)',fontsize=16)
################################################################################3


# Create another legend for the second line.
#plt.legend(handles=[eccen_plot], loc='lower right',
#           title="$\\bf{Eccentric \ Planets}$", title_fontsize=15, prop={'size': 15}, fancybox=True)

plt.grid(True, alpha=0.35)
plt.ylabel(r"Planet Gravity [$m/s^2$]", fontsize=18, fontweight = 'bold')
plt.xlabel("Planet Period [days]", fontsize=18 , fontweight = 'bold')
plt.title("Planets Observed with Phase Curves", fontsize=24 , fontweight = 'bold')
plt.yscale('log')
plt.xscale('log')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.savefig(save_dir + 'JWST-Ariel-pg_porb_fom.jpg')

plt.show()

###############################################
fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel_4cat['Planet Temperature [K]'].min(), ariel_4cat['Planet Temperature [K]'].max()
# cmap='viridis_r'
cmap = 'RdYlBu_r'

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")["pl_radj"], pc_telescope.query("JWST == 'Yes'")['pl_orbper'],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_eqt"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=1, vmin=min_, vmax=max_)

Ariel_plot = ax.scatter(ariel_4cat["Planet Radius [Rj]"], ariel_4cat['Planet Period [days]'],
                        alpha=1, s = 200, c = ariel_4cat["Planet Temperature [K]"], marker="*",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 2, vmin=min_, vmax=max_)

clb = fig.colorbar(JWST_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planetary Equilibrium Temperature [K]',fontsize=16)

ax.axvline(0.160586, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axvline(0.312251, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axvline(0.624503, color='g', linestyle='dashed', linewidth=1, alpha=1)


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
plt.xlabel('Planet Radius [R$_J$]', fontsize=24, fontweight='bold')
plt.ylabel("Planet Period [days]", fontsize=28, fontweight='bold')
plt.title("Phase Curves Targets", fontsize=28, fontweight='bold')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+ 'JWST-Ariel-Phasecurves-allcat.jpg')

plt.show()
plt.close()