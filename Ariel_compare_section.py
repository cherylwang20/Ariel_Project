from Tier_2_target_analysis import *
from Ariel_bestt_4cat import *


period = target_45['Planet Period [days]']
N_obs_rfm = target_45['N obs']
N_obs_bic = ariel_4cat['N obs']
#transit = target_45['Transit Duration [s]']
AESM_rfm = target_45['Tier2_SNR']
AESM_bic = ariel_4cat['Tier2_SNR']

print(AESM.min())

bins = 15
fig, (ax1, ax2) = plt.subplots(1, 2, sharey= True, figsize=(15, 10))
ax1.set_xlabel(r"$N_{obs}$", fontsize=24, fontweight='bold')
ax1.set_ylabel("# of planets", fontsize=24, fontweight='bold')
ax1.tick_params(axis="x", labelsize=17)
ax1.tick_params(axis="y", labelsize=17)
ax1.set_xscale('log')
his, bin = np.histogram(N_obs_bic, bins=bins)
logbin = np.logspace(np.log10(bin[0]),np.log10(bin[-1]),len(bin))
ax1.hist([N_obs_rfm, N_obs_bic], bins= logbin, rwidth=3,
         color = ['deepskyblue', 'orange'], label= ['Ranked FoM', 'Best in Class'])
ax1.legend(prop={'size': 18})



plt.xlabel("Tier 2 AESM", fontsize=24, fontweight='bold')
plt.ylabel("# of planets", fontsize=24, fontweight='bold')
#plt.title("Histogram of 42 selected targets", fontsize=24, fontweight='bold')


hist, bins = np.histogram(AESM_bic, bins=bins)
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
ax2.hist([AESM_rfm, AESM_bic], bins = logbins, rwidth= 0.85,
         color = ['deepskyblue', 'orange'], label= ['Ranked FoM', 'Best in Class'])
#fig.suptitle("Histogram of 42 selected targets", fontsize=24, fontweight='bold')
plt.xscale('log')
ax2.legend(prop={'size': 18})
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.savefig(save_dir + 'Ariel_histogram_compare.pdf')

plt.show()
plt.close()

######################################