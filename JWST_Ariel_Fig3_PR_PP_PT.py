from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel['Planet Temperature [K]'].min(), ariel['Planet Temperature [K]'].max()
# cmap='viridis_r'
cmap = 'RdYlBu_r'

print(len(ariel))

JWST_plot = ax.scatter( pc_telescope.query("JWST == 'Yes'")['pl_orbper'],pc_telescope.query("JWST == 'Yes'")["pl_radj"],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")["pl_eqt"], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=2, vmin=min_, vmax=max_)

Ariel_plot = ax.scatter( ariel['Planet Period [days]'],ariel["Planet Radius [Rj]"],
                        alpha=1, s = 200, c = ariel["Planet Temperature [K]"], marker="*",
                        edgecolor='black', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 1, vmin=min_, vmax=max_)

clb = fig.colorbar(JWST_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planetary Equilibrium Temperature [K]',fontsize=16)

ax.axhline(0.160586, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axhline(0.312251, color='g', linestyle='dashed', linewidth=1, alpha=1)
ax.axhline(0.624503, color='g', linestyle='dashed', linewidth=1, alpha=1)

'''
for x, y, name in zip(pc_telescope.query("JWST == 'Yes'")["pl_radj"], pc_telescope.query("JWST == 'Yes'")["pl_orbper"],
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
'''
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
plt.savefig(save_dir+ 'JWST-Ariel-Phasecurves-target.pdf')

plt.show()