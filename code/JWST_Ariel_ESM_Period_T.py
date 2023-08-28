from phasecurve_plot_cheryl import *
import matplotlib

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = ariel.ESM.min(), ariel.ESM.max()
print(min_,max_)
# cmap='viridis_r'
cmap = 'cool'
JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")["pl_orbper"], pc_telescope.query("JWST == 'Yes'")["pl_eqt"],
                       alpha=1, s=850, c=pc_telescope.query("JWST == 'Yes'")['ESM'], marker='h', edgecolor='black',
                       cmap=cmap,norm=matplotlib.colors.LogNorm(vmin=min_, vmax=max_),
                       label='JWST', zorder=2)

Ariel_plot = ax.scatter( ariel['Planet Period [days]'], ariel["Planet Temperature [K]"],
                        alpha=0.8, s = 100, c = ariel["ESM"], marker="*",
                        edgecolor='black', cmap=cmap,norm=matplotlib.colors.LogNorm( vmin=min_, vmax=max_),
                        linewidths=1, label = "Ariel", zorder = 1)

# ax.set_clim(min_, max_)
clb = fig.colorbar(Ariel_plot, ax=ax)  # .set_label('$\\bf{ESM} $',rotation=270,fontsize=15)
clb.ax.set_title('$\\bf{ESM} $')

pc_telescope['T_max'] = pc_telescope['pl_eqt'] / np.sqrt(1 - pc_telescope['pl_orbeccen'])
pc_telescope['T_min'] = pc_telescope['pl_eqt'] / np.sqrt(1 + pc_telescope['pl_orbeccen'])

# eccen_plot = ax.hlines('pl_g', 'T_min', 'T_max', data = pc_telescope.query("pl_orbeccen > 0.09"), lw=3, label = 'Temperature Range')


for x, y, name in zip(pc_telescope.query("JWST == 'Yes'")["pl_orbper"], pc_telescope.query("JWST == 'Yes'")["pl_eqt"],
                      pc_telescope.query("JWST == 'Yes'")["pl_name"]):

    label = name

    if label == 'WASP-121 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, -15),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    elif label == 'GJ 1214 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, -25),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    elif label == 'LTT 9779 b':
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, -15),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    elif label == 'HD 80606 b':
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
ax.axvline(2, color='blue', linestyle='dashed', linewidth=2, alpha=0.75)


from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def getImage(path, zoom):
    return OffsetImage(plt.imread(path), zoom=zoom)


paths = [
    'Earth.png',
    'Jupiter.png',
    'neptune.jpg']

full_paths = [os.path.join(save_dir, path) for path in paths]



zooms = [0.025, 0.065, 0.15]
SS_eqt = [279,  # Earth
          122,  # Jupiter
          51]  # Neptune

SS_g = [9.8,  # Earth
        24.8,  # Jupiter
        11.5]  # Neptune

ax.scatter( SS_orb, SS_eqt)

for x0, y0, path, z in zip( SS_orb,SS_eqt, full_paths, zooms):
    ab = AnnotationBbox(getImage(path, z), (x0, y0), frameon=False)
    ax.add_artist(ab)

############################################################33

# Create a legend for the first line.
# first_legend = plt.legend(handles=[Spitzer_plot,Hubble_plot, JWST_plot], loc='upper right',
#                           title = "$\\bf{Telescope} $", title_fontsize = 20, prop={'size': 20}, fancybox = True)


from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='h', color='w', label='JWST',
                          markerfacecolor='none', markeredgecolor='black', mew=3, markersize=25),
                   Line2D([0], [0], marker='*', color='w', label='Ariel',
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
plt.ylabel("Planetary Equilibrium Temperature [K]", fontsize=18, fontweight='bold')
plt.xlabel("Planet Period [days]", fontsize=18, fontweight='bold')
plt.title("Planets Observed with Phase Curves", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.xscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'JWST-Ariel-Phasecurves-ESM-T.pdf')

plt.show()