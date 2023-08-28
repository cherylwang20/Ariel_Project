from Tier_2_target_analysis import *

angle = 45
curve_df, fc, pc = new_cum_time(ariel_sort_eclipse_num, angle)

total = fc+pc

ariel_sort_Tier3 = ariel.sort_values(by = 'Tier 3 Eclipses').head(total)

print(ariel_sort_Tier3)

ariel_Tier2 = ariel_sort_Tier3[ariel_sort_Tier3['Tier 2 Emission'] == 1]
ariel_Tier2_n = ariel_sort_Tier3[ariel_sort_Tier3['Tier 2 Emission'] == 0]

print(ariel_Tier2)

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel_sort_Tier3['Planet Temperature [K]'].min(), ariel_sort_Tier3['Planet Temperature [K]'].max()
# cmap='viridis_r'
cmap = 'RdYlBu_r'

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")["pl_radj"], pc_telescope.query("JWST == 'Yes'")['pl_orbper'],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_eqt"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=2, vmin=min_, vmax=max_)

Ariel_plot_1 = ax.scatter(ariel_Tier2["Planet Radius [Rj]"], ariel_Tier2['Planet Period [days]'],
                        alpha=1, s = 200, c = ariel_Tier2["Planet Temperature [K]"], marker="*",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel Tier 2", zorder = 2, vmin=min_, vmax=max_)

Ariel_plot_2= ax.scatter(ariel_Tier2_n["Planet Radius [Rj]"], ariel_Tier2_n['Planet Period [days]'],
                        alpha=0.5, s = 100, c = 'grey', marker="o",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel Tier 2, S/N < 7", zorder = 1, vmin=min_, vmax=max_)

clb = fig.colorbar(JWST_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planetary Equilibrium Temperature [K]',fontsize=16)

ax.axvline(0.160586, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axvline(0.312251, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axvline(0.624503, color='g', linestyle='dashed', linewidth=1, alpha=1)


from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='h', color='w', label='JWST',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                   Line2D([0], [0], marker='*', color='w', label='Ariel Tier 2',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                    Line2D([0], [0], marker='o', color='w', label='Ariel Tier 2, S/N < 7',
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
plt.savefig(save_dir+ 'JWST-Ariel-Phasecurves-cul365.jpg')

plt.show()
plt.close()