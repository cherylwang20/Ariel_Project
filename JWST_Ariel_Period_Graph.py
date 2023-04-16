from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))

JWST_plot = ax.scatter(pc_telescope.query("JWST == 'Yes'")["pl_orbper"], pc_telescope.query("JWST == 'Yes'")["pl_eqt"],
                       edgecolor= 'black', alpha=1, s=850, c='gold', marker='h', label='JWST', zorder=2)

Ariel_plot = ax.scatter(ariel["Planet Period [days]"], ariel['Planet Temperature [K]'],
                        alpha=0.4, s = 200, c = "green", marker="*",
                        edgecolor= 'green', label = "Ariel", zorder = 1)


for x, y, name in zip(pc_telescope.query("JWST == 'Yes'")["pl_orbper"], pc_telescope.query("JWST == 'Yes'")["pl_eqt"],
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

    else:
        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 15),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
############################

ax.axvline(3, color ='blue', lw = 4, alpha = 0.75)

################################################################################3

from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def getImage(path, zoom):
    return OffsetImage(plt.imread(path), zoom=zoom)


paths = [
    'Earth.png',
    'Jupiter.png',
    'neptune.jpg']

zooms = [0.025, 0.065, 0.15]


ax.scatter(SS_orb, SS_eqt)

for x0, y0, path, z in zip(SS_orb, SS_eqt, paths, zooms):
    ab = AnnotationBbox(getImage(path, z), (x0, y0), frameon=False)
    ax.add_artist(ab)

############################################################33

# Create a legend for the first line.
first_legend = plt.legend(handles=[JWST_plot, Ariel_plot], loc='upper right',
                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)

plt.grid(True, alpha=0.35)
plt.ylabel("Planetary Equilibrium Temperature [K]", fontsize=22, fontweight='bold')
plt.xlabel("Planet Orbital Period [Days]", fontsize=22, fontweight='bold')
plt.title("Planets Observed with Phase Curves", fontsize=26, fontweight='bold')
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
# plt.ylim([0,105])
plt.savefig('JWST-Ariel-PhaseCurvePlot-Orb-K.pdf')

plt.show()