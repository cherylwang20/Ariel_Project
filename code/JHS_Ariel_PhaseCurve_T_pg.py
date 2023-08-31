'''
@author: Huiyi (Cheryl) Wang
August 2023

Graphing Hubble - Spizter - JWST-Ariel-Phasecurves
temperature - gravity - ESM
'''


import matplotlib.pyplot as plt

from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = pc_telescope.ESM.min(), pc_telescope.ESM.max()
# cmap='viridis_r'
cmap = 'cool'
Spitzer_plot = ax.scatter(pc_telescope.query("Spitzer == 'Yes'")["pl_eqt"],
                          pc_telescope.query("Spitzer == 'Yes'")["pl_g"],
                          alpha=1, s=250, c=pc_telescope.query("Spitzer == 'Yes'")['ESM'], marker="P",
                          edgecolor='black', cmap=cmap,
                          linewidths=1, label="Spitzer", zorder=4, vmin=0, vmax=max_)

Hubble_plot = ax.scatter(pc_telescope.query("Hubble == 'Yes'")["pl_eqt"], pc_telescope.query("Hubble == 'Yes'")["pl_g"],
                         alpha=1, s=350, c=pc_telescope.query("Hubble == 'Yes'")['ESM'], marker='X', edgecolor='black',
                         cmap=cmap,
                         linewidths=1, label='Hubble', zorder=3, vmin=0, vmax=max_)

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")["pl_eqt"], pc_telescope.query("JWST == 'Yes'")["pl_g"],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")['ESM'], marker='h', edgecolor='black',
                       cmap=cmap,
                       label='JWST', zorder=2, vmin=0, vmax=max_)

Ariel_plot = ax.scatter(ariel_ESM_100["Planet Temperature [K]"], ariel_ESM_100['pl_g'],
                        alpha=0.4, s = 100, c = "grey", marker="o",
                        edgecolor='grey', cmap=cmap,
                        linewidths=1, label = "Ariel", zorder = 1, vmin=0, vmax=max_)

# ax.set_clim(min_, max_)
clb = fig.colorbar(Spitzer_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
clb.ax.set_title('$\\bf{ESM} $')

pc_telescope['T_max'] = pc_telescope['pl_eqt'] / np.sqrt(1 - pc_telescope['pl_orbeccen'])
pc_telescope['T_min'] = pc_telescope['pl_eqt'] / np.sqrt(1 + pc_telescope['pl_orbeccen'])

# eccen_plot = ax.hlines('pl_g', 'T_min', 'T_max', data = pc_telescope.query("pl_orbeccen > 0.09"), lw=3, label = 'Temperature Range')


for x, y, name in zip(pc_telescope.query("JWST == 'Yes'")["pl_eqt"], pc_telescope.query("JWST == 'Yes'")["pl_g"],
                      pc_telescope.query("JWST == 'Yes'")["pl_name"]):

    label = name

    if label == 'WASP-121 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(20, 15),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    elif label == 'GJ 1214 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(10, -25),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    elif label == 'LTT 9779 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(-15, 15),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    elif label == 'HD 80606 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, -25),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    elif label == "TRAPPIST-1 b":
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(-20, -25),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    else:
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 15),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

## Label HD 189
'''
for x, y, name in zip(pc_telescope.query("pl_name == 'HD 189733 b'")["pl_eqt"],
                      pc_telescope.query("pl_name == 'HD 189733 b'")["pl_radj"],
                      pc_telescope.query("pl_name == 'HD 189733 b'")["pl_name"]):
    label = name

    plt.annotate(label,  # this is the text
                 (x, y),  # these are the coordinates to position the label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 0),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center
'''
################################################################################3

from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def getImage(path, zoom):
    return OffsetImage(plt.imread(path), zoom=zoom)


paths = [
    'Jupiter.png',
    'neptune.jpg']

zooms = [ 0.065, 0.15]
SS_eqt = [ # Earth
          122,  # Jupiter
          51]  # Neptune

SS_g = [ # Earth
        24.8,  # Jupiter
        11.5]  # Neptune

ax.scatter(SS_eqt, SS_g)

for x0, y0, path, z in zip(SS_eqt, SS_g, paths, zooms):
    ab = AnnotationBbox(getImage(path, z), (x0, y0), frameon=False)
    ax.add_artist(ab)

############################################################33

# Create a legend for the first line.
# first_legend = plt.legend(handles=[Spitzer_plot,Hubble_plot, JWST_plot], loc='upper right',
#                           title = "$\\bf{Telescope} $", title_fontsize = 20, prop={'size': 20}, fancybox = True)


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

first_legend = plt.legend(handles=legend_elements, loc='upper right',
                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)

# # Create another legend for the second line.
# plt.legend(handles=[eccen_plot], loc='lower right',
#           title = "$\\bf{Eccentric \ Planets}$", title_fontsize = 15, prop={'size': 15}, fancybox = True)


plt.grid(True, alpha=0.35)
plt.xlabel("Planetary Equilibrium Temperature [K]", fontsize=18, fontweight='bold')
plt.ylabel(r"Planet Gravity [$m/s^2$]", fontsize=18, fontweight='bold')
plt.title("Planets Observed with Phase Curves", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'JWST-Ariel-Phasecurves-Plg.jpg')

plt.show()