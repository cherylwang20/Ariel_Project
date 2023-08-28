'''
@author: Huiyi (Cheryl) Wang
August 2023

The code serve as the backup of calculations made by not documented within the Ariel Project PDF
'''


from phasecurve_plot_cheryl import *


############ this is day/night side constrast with Taylor's data
selected_sample = jupiter_temp.merge(ariel, on='Planet Name',how = 'left')


selected_sample['ESM High'] = ESM(selected_sample['T day (K)'], selected_sample["Star Temperature [K]"], selected_sample["Planet Radius [Rj]"],
                   selected_sample["Star Radius [Rs]"], selected_sample["Star K Mag"])
selected_sample['ESM Low'] = ESM(selected_sample['T night (K)'], selected_sample["Star Temperature [K]"], selected_sample["Planet Radius [Rj]"],
                   selected_sample["Star Radius [Rs]"], selected_sample["Star K Mag"])

# calculate the ariel emission metric for all ariel targets
row_list = []

for i, row in ariel.iterrows():
    row_list.append(SNR_Ariel(1/24, row['Star Radius [Rs]'], row['Star Distance [pc]'],
                         row['Star Temperature [K]'],lamb_1_ariel, lamb_2_ariel, row['Planet Radius [Rj]'],
                         row['Planet Temperature [K]'])) #row['Planet Period [days]']
#print(row_list)
ariel['ASM'] = pd.DataFrame(row_list)





############ calculate the ASM of the exoplanets in Bell (2021)
row_list = []

for i, row in selected_sample.iterrows():
    row_list.append(SNR_Ariel(1/24, row['Star Radius [Rs]'], row['Star Distance [pc]'],
                         row['Star Temperature [K]'],lamb_1_ariel, lamb_2_ariel, row['Planet Radius [Rj]'],
                         row['T day (K)'])) #row['Planet Period [days]']
#print(row_list)
selected_sample['ASM High'] = pd.DataFrame(row_list)


row_list = []

for i, row in selected_sample.iterrows():
    row_list.append(SNR_Ariel(1/24, row['Star Radius [Rs]'], row['Star Distance [pc]'],
                         row['Star Temperature [K]'],lamb_1_ariel, lamb_2_ariel, row['Planet Radius [Rj]'],
                         row['T night (K)'])) #row['Planet Period [days]']
#print(row_list)
selected_sample['ASM Low'] = pd.DataFrame(row_list)



selected_sample.to_csv(data_dir + 'selected_target.csv')


###############
#sort according to the shortest orbit and filter out the 10%
cut_off = 2000

ariel_sort_so = cum_df(ariel.sort_values('Planet Period [days]'))


#sort according to the highest ESM or maybe try with # of terrestrial bins
ariel_sort_ESM = cum_df(ariel.sort_values(by = 'ESM',ascending=False))
ariel_sort_ESM.to_csv(data_dir + 'ESM_Ariel_sort.csv')
ariel_ESM_100 = ariel_sort_ESM.head(100)

############################################3
# sort Ariel according to Eclipse
ariel_sort_eclipse_num = cum_df(ariel.sort_values('Tier 3 Eclipses'))
ariel_sort_eclipse_num.to_csv(data_dir + 'Eclipse_Cum.csv')
ariel_eclipse_100 = ariel_sort_eclipse_num.head(100)

# sort according to the highest ASM and see if this matches with the highest # of bins.
ariel_sort_ASM = cum_df(ariel.sort_values(by = 'ASM',ascending=False))
ariel_sort_ASM.to_csv(data_dir + 'ASM_Ariel_sort.csv')

######################## rank everything based on tier 3 transits

ariel_sort_transit_num = ariel.sort_values('Tier 3 Transits')
ariel_transit_100 = ariel_sort_transit_num.head(100)

######### see if the highest
overlap_target = cum_df_transit(pd.merge(ariel_transit_100, ariel_eclipse_100, how = "inner"))
overlap_target_selected = overlap_target[["Planet Name","Tier 3 Eclipses","Tier 3 Transits",
                                           "Planet Period [days]", "Transit Duration [s]", 'cumulative transit time [days]' ]]
overlap_target_selected.to_csv(data_dir + 'overlap.csv')




################ sort ariel into different mass range:
ariel_terrestrial = ariel.loc[ariel['Planet Radius [Rj]'] <= 0.16058]
ariel_subnep = ariel.loc[(ariel['Planet Radius [Rj]'] >= 0.16058)
                & (ariel['Planet Radius [Rj]'] <= 0.312251)]
ariel_nep = ariel.loc[(ariel['Planet Radius [Rj]'] <= 0.624503)
                & (ariel['Planet Radius [Rj]'] >= 0.312251)]
ariel_giant = ariel.loc[ariel['Planet Radius [Rj]'] >= 0.624503]

############## create df of partial phase curve and full phase curve for 45 degree phase curve
curve_df = new_cum_time(ariel_sort_eclipse_num,45)[0]
ariel_full = curve_df[curve_df['Planet Period [days]']<= 2]
ariel_partial = curve_df[curve_df['Planet Period [days]'] > 2]