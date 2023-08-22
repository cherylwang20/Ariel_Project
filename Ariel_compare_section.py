from Tier_2_target_analysis import *
from Ariel_bestt_4cat import *

target_45 = new_cum_time(Tier_2_target, 45, False)[0]

print(target_45['Tier2_SNR'].min())

period = target_45['Planet Period [days]']
#transit = target_45['Transit Duration [s]']
AESM = target_45['Tier2_SNR']

print(AESM.min())

bins = 15
fig, (ax1, ax2) = plt.subplots(1, 2, sharey= True, figsize=(18, 10))
ax1.set_xlabel("Planet Period [days]", fontsize=22, fontweight='bold')
ax1.set_ylabel("# of planets", fontsize=22, fontweight='bold')
ax1.tick_params(axis="x", labelsize=17)
ax1.tick_params(axis="y", labelsize=17)
ax1.axvline(2, linestyle = 'dashed', color = 'cyan', linewidth = 3)
#ax1.set_xlim(xmin=0, xmax = 26)
ax1.hist(period, bins= bins, rwidth= 0.85, color = 'green')



plt.xlabel("Tier 2 AESM", fontsize=22, fontweight='bold')
plt.ylabel("# of planets", fontsize=22, fontweight='bold')
#plt.title("Histogram of 42 selected targets", fontsize=24, fontweight='bold')


hist, bins = np.histogram(AESM, bins=bins)
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
ax2.hist(AESM, bins = logbins, rwidth= 0.85, color= 'red')
#fig.suptitle("Histogram of 42 selected targets", fontsize=24, fontweight='bold')
plt.xscale('log')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)

plt.savefig(save_dir + 'Ariel_histogram_365d.pdf')

plt.show()