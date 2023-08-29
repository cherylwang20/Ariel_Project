'''
@author: Huiyi (Cheryl) Wang
August 2023

This code looks at the best in class method when observing all targets for only once
'''



from phasecurve_plot_cheryl import *

ariel_cal = pd.read_csv(os.path.join(data_dir, 'SNR_all_tier.csv'))

ariel_cal = ariel_cal.sort_values(by = 'Tier1_SNR',ascending=False)
num = 6

############# we first calculate the cumulative time of observation for each class
## of target, and then we find the top targets within 1/4 of a year
###### we then see how many targets is observable given those circumstances.'

## keep in mind that we should consider partial phase curves
ariel_terrestrial = new_cum_time(ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] <= 0.16058)])[0]
ariel_t_1 = cum_df(ariel_terrestrial)
ariel_t_1 = ariel_t_1[ariel_t_1['cumulative days'] < 365 / 4]

ariel_subnep = new_cum_time(ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] >= 0.16058)
                & (ariel_cal['Planet Radius [Rj]'] <= 0.312251)])[0]
ariel_sp_1 = cum_df(ariel_subnep)
ariel_sp_1 = ariel_sp_1[ariel_sp_1['cumulative days'] < 365 / 4]

ariel_nep = new_cum_time(ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] <= 0.624503)
                & (ariel_cal['Planet Radius [Rj]'] >= 0.312251) ])[0]
ariel_n_1 = cum_df(ariel_nep)
ariel_n_1 = ariel_n_1[ariel_n_1['cumulative days'] < 365 / 4]

ariel_giant = new_cum_time(ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] >= 0.624503)  & (ariel_cal['Tier2_SNR'] >= 7)])[0]
ariel_g_1 = cum_df(ariel_giant)
ariel_g_1 = ariel_g_1[ariel_g_1['cumulative days'] < 365 / 4]

ariel_terrestrial = ariel_terrestrial[ariel_terrestrial['New Cumulative Days'] < 365/4]
ariel_subnep = ariel_subnep[ariel_subnep['New Cumulative Days'] < 365/4]
ariel_nep = ariel_nep[ariel_nep['New Cumulative Days'] < 365/4]
ariel_giant = ariel_giant[ariel_giant['New Cumulative Days'] < 365/4]

print(len(ariel_t_1), len(ariel_sp_1), len(ariel_n_1), len(ariel_g_1))
print(len(ariel_terrestrial), len(ariel_subnep), len(ariel_nep), len(ariel_giant))

ariel_4cat_45 = pd.concat([ariel_terrestrial, ariel_subnep,
                        ariel_nep,ariel_giant])

ariel_4cat_full = pd.concat([ariel_g_1, ariel_n_1, ariel_sp_1, ariel_t_1])

print(ariel_4cat_45['Tier2_SNR'].mean())

################ we do this for 90 degree

ariel_terrestrial = new_cum_time(ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] <= 0.16058)], 90)[0]


ariel_subnep = new_cum_time(ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] >= 0.16058)
                & (ariel_cal['Planet Radius [Rj]'] <= 0.312251)], 90)[0]

ariel_nep = new_cum_time(ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] <= 0.624503)
                & (ariel_cal['Planet Radius [Rj]'] >= 0.312251)], 90 )[0]

ariel_giant = new_cum_time(ariel_cal.loc[(ariel_cal['Planet Radius [Rj]'] >= 0.624503)  & (ariel_cal['Tier2_SNR'] >= 7)], 90)[0]


ariel_terrestrial = ariel_terrestrial[ariel_terrestrial['New Cumulative Days'] < 365/4]
ariel_subnep = ariel_subnep[ariel_subnep['New Cumulative Days'] < 365/4]
ariel_nep = ariel_nep[ariel_nep['New Cumulative Days'] < 365/4]
ariel_giant = ariel_giant[ariel_giant['New Cumulative Days'] < 365/4]
print(len(ariel_terrestrial), len(ariel_subnep), len(ariel_nep), len(ariel_giant))

ariel_4cat_90 = pd.concat([ariel_terrestrial, ariel_subnep,
                        ariel_nep,ariel_giant])


#####################
fig, ax = plt.subplots(figsize=(15, 10))

ariel_4cat_45, fc, pc = new_cum_time(ariel_4cat_45, 45)
ax.plot(list(range(len(ariel_4cat_45))), ariel_4cat_45['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{45}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')


ariel_4cat_90, fc, pc = new_cum_time(ariel_4cat_90, 90)
ax.plot(list(range(len(ariel_4cat_90))), ariel_4cat_90['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{90}°, full = {fc}, partial = {pc}',
                            linestyle='dashdot')

ariel_4cat_full = cum_df(ariel_4cat_full)
print('average AESM for full', ariel_4cat_full['Tier2_SNR'].mean())
Ariel_eclipse = ax.plot(list(range(len(ariel_4cat_full))), ariel_4cat_full['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       color = 'black')


plt.grid(True, alpha=0.35)
plt.xlabel("# of planets", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
#plt.title("Ariel Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = r"Partial Observing Angle $\theta$ (°)", loc = "lower right", fontsize = 15, title_fontsize= 15)
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Tier2_allcat_n1.pdf')

plt.show()
plt.close()