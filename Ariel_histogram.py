import pandas as pd

from phasecurve_plot_cheryl import *

ft_target = pd.read_csv(os.path.join(data_dir, 'selected_target_42.csv'))

period = ft_target['Planet Period [days]']
transit = ft_target['Transit Duration [s]']


fig, (ax1, ax2) = plt.subplots(1, 2, sharey= True, figsize=(18, 10))
ax1.set_xlabel("Planet Period [days]", fontsize=20, fontweight='bold')
ax1.set_ylabel("# of planets", fontsize=20, fontweight='bold')
ax1.tick_params(axis="x", labelsize=17)
ax1.tick_params(axis="y", labelsize=17)
ax1.hist(period, bins= 'auto', rwidth= 0.85, color = 'green')


plt.xlabel("Transit Duration [hrs]", fontsize=20, fontweight='bold')
plt.ylabel("# of planets", fontsize=20, fontweight='bold')
#plt.title("Histogram of 42 selected targets", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
ax2.hist(transit*3/3600, bins = 'auto', rwidth= 0.85, color= 'red')
#fig.suptitle("Histogram of 42 selected targets", fontsize=24, fontweight='bold')

plt.savefig(save_dir + 'Ariel_histogram.pdf')

plt.show()