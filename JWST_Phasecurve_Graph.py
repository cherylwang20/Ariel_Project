from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = pc_telescope.pl_radj.min(), pc_telescope.pl_radj.max()
# cmap='viridis_r'
cmap = 'cool'


Spitzer_plot = ax.scatter(pc_telescope.query("Spitzer == 'Yes'")["pl_eqt"],
                          pc_telescope.query("Spitzer == 'Yes'")['ESM'],
                          alpha=1, s=250, c=pc_telescope.query("Spitzer == 'Yes'")["pl_radj"], marker="P",
                          edgecolor='black', cmap=cmap,
                          linewidths=1, label="Spitzer", zorder=4, vmin=min_, vmax=max_)

Hubble_plot = ax.scatter(pc_telescope.query("Hubble == 'Yes'")["pl_eqt"], pc_telescope.query("Hubble == 'Yes'")['ESM'],
                         alpha=1, s=350, c=pc_telescope.query("Hubble == 'Yes'")["pl_radj"], marker='X',
                         edgecolor='black', cmap=cmap,
                         linewidths=1, label='Hubble', zorder=3, vmin=min_, vmax=max_)

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")["pl_eqt"], pc_telescope.query("JWST == 'Yes'")['ESM'],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_radj"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=2, vmin=min_, vmax=max_)

print(ariel_sort_ESM.head(100))


Ariel_plot = ax.scatter(ariel_ESM_100["Planet Temperature [K]"], ariel_ESM_100['ESM'],
                        alpha=0.4, s = 100, c = "grey", marker="o",
                        edgecolor='grey', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 1, vmin=min_, vmax=max_)

#ariel["Planet Radius [Rj]"]
# ax.set_clim(min_, max_)
clb = fig.colorbar(Spitzer_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
clb.ax.set_title('Planet Radius [R$_J$]', fontweight='bold')

pc_telescope['T_max'] = pc_telescope['pl_eqt'] / np.sqrt(1 - pc_telescope['pl_orbeccen'])
pc_telescope['T_min'] = pc_telescope['pl_eqt'] / np.sqrt(1 + pc_telescope['pl_orbeccen'])

# eccen_plot = ax.hlines('pl_g', 'T_min', 'T_max', data = pc_telescope.query("pl_orbeccen > 0.09"), lw=3, label = 'Temperature Range')


for x, y, name in zip(pc_telescope.query("JWST == 'Yes'")["pl_eqt"], pc_telescope.query("JWST == 'Yes'")["ESM"],
                      pc_telescope.query("JWST == 'Yes'")["pl_name"]):

    label = name

    if label == 'WASP-121 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 20),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    elif label == 'GJ 1214 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(-20, 15),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    elif label == 'LTT 9779 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(10, 20),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    elif label == 'HD 80606 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(35, -20),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    elif label == 'NGTS-10 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, -25),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    else:
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, -25),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='P', color='w', label='Spitzer',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                   Line2D([0], [0], marker='X', color='w', label='Hubble',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                   Line2D([0], [0], marker='h', color='w', label='JWST',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                   Line2D([0], [0], marker='o', color='w', label='Ariel',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25)
                   ]

first_legend = plt.legend(handles=legend_elements, loc='lower right',
                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)

plt.grid(True, alpha=0.35)
plt.xlabel("Planetary Equilibrium Temperature [K]", fontsize=24, fontweight='bold')
plt.ylabel("Emission Spectroscopy Metric", fontsize=28, fontweight='bold')
plt.title("Planets Observed with Phase Curves", fontsize=28, fontweight='bold')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.yscale('log')
# plt.ylim([0,105])
#plt.savefig('JWST-Phasecurves-ESM-largertext.pdf')
plt.savefig(save_dir+'JWST-Ariel-Phasecurves-ESM-largertext.jpg')

plt.show()