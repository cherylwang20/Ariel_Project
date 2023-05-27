from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))

Spitzer_plot = ax.scatter(pc_telescope.query("Spitzer == 'Yes'")["pl_eqt"],
                          pc_telescope.query("Spitzer == 'Yes'")["pl_g"],
                          alpha=1, s=350, c='red', marker="+", linewidths=4, label="Spitzer", zorder=4)

Hubble_plot = ax.scatter(pc_telescope.query("Hubble == 'Yes'")["pl_eqt"], pc_telescope.query("Hubble == 'Yes'")["pl_g"],
                         alpha=1, s=350, c='blue', marker='x', linewidths=4, label='Hubble', zorder=3)

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")["pl_eqt"], pc_telescope.query("JWST == 'Yes'")["pl_g"],
                       alpha=1, s=850, c='gold', marker='h', label='JWST', zorder=2)

Ariel_plot = ax.scatter(ariel_eclipse_100["Planet Temperature [K]"], ariel_eclipse_100['pl_g'],
                        alpha=0.4, s = 150, c = "grey", marker="o",
                        label = "Ariel", zorder = 1)

pc_telescope['T_max'] = pc_telescope['pl_eqt'] / np.sqrt(1 - pc_telescope['pl_orbeccen'])
pc_telescope['T_min'] = pc_telescope['pl_eqt'] / np.sqrt(1 + pc_telescope['pl_orbeccen'])

eccen_plot = ax.hlines('pl_g', 'T_min', 'T_max', data=pc_telescope.query("pl_orbeccen > 0.09"), lw=3,
                       label='Temperature Range')

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
                     xytext=(-25, -25),  # distance from text to points (x,y)
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


SS_eqt = [
          122,  # Jupiter
          51]  # Neptune

SS_g = [
        24.8,  # Jupiter
        11.5]  # Neptune

ax.scatter(SS_eqt, SS_g)

for x0, y0, path, z in zip(SS_eqt, SS_g, paths, zooms):
    ab = AnnotationBbox(getImage(path, z), (x0, y0), frameon=False)
    ax.add_artist(ab)

############################################################33

# Create a legend for the first line.
first_legend = plt.legend(handles=[Spitzer_plot, Hubble_plot, JWST_plot, Ariel_plot], loc='upper right',
                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)

# Create another legend for the second line.
plt.legend(handles=[eccen_plot], loc='lower right',
           title="$\\bf{Eccentric \ Planets}$", title_fontsize=15, prop={'size': 15}, fancybox=True)

plt.grid(True, alpha=0.35)
plt.xlabel("Planetary Equilibrium Temperature [K]", fontsize=18)
plt.ylabel("Planet Gravity [$g$]", fontsize=18)
plt.title("Planets Observed with Phase Curves", fontsize=24)
plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'JWST-Ariel-PhaseCurvePlot-eccen-Gravity.jpg')

plt.show()