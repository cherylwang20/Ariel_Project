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




######### see if the highest
overlap_target = cum_df_transit(pd.merge(ariel_transit_100, ariel_eclipse_100, how = "inner"))
overlap_target_selected = overlap_target[["Planet Name","Tier 3 Eclipses","Tier 3 Transits",
                                           "Planet Period [days]", "Transit Duration [s]", 'cumulative transit time [days]' ]]
overlap_target_selected.to_csv(data_dir + 'overlap.csv')




