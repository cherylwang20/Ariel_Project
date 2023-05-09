from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))

ariel_ESM_high = ariel.loc[ariel['ESM'] > 7.5]
ariel_ESM_low = ariel.loc[ariel['ESM'] <= 7.5]

ariel_ESM_high['Spectral Type'] = ariel_ESM_high['Star Spectral Type'].str[0]

#create a dictionary for different spectrum
colors = {'O': 'violet', 'B': 'mediumblue', 'A': 'lightblue', 'F': 'lawngreen', 'G': 'yellow', 'K': 'orange', 'M': 'orangered', np.nan: 'grey'}


Ariel_low_plot = ax.scatter(ariel_ESM_low["Planet Temperature [K]"], ariel_ESM_low['Planet Period [days]'],
                        alpha=0.4, s = 50, c = "pink", marker="o",
                        label = "Ariel", zorder = 1)
Ariel_ESM_plot = ax.scatter(ariel_ESM_high["Planet Temperature [K]"], ariel_ESM_high['Planet Period [days]'],
                        alpha=0.9, s = 150, c = ariel_ESM_high['Spectral Type'].apply(lambda  x: colors[x]),
                        edgecolor= 'white', marker="o", zorder = 2)


# Create a legend for the first line.
#first_legend = plt.legend(handles=[JWST_plot, Ariel_plot], loc='upper right',
#                          title="$\\bf{Telescope} $", title_fontsize=20, prop={'size': 20}, fancybox=True)

# Add the legend manually to the current Axes.
#ax = plt.gca().add_artist(first_legend)
legend_elements = [plt.scatter([], [], marker='o', color=color,  label=spec) for spec, color in colors.items()]
plt.legend(handles=legend_elements, title='Spectral Type',   loc='upper right')


plt.grid(True, alpha=0.35)
plt.xlabel("Planetary Equilibrium Temperature [K]", fontsize=18)
plt.ylabel("Planet Period [days]", fontsize=18)
plt.title("Ariel Phase Curve Targets: Temperature vs Period", fontsize=24)
plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-PhaseCurve-Temp-Per.jpg')

plt.show()