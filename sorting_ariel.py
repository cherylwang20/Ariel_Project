from phasecurve_plot_cheryl import *

#sort according to the shortest orbit and filter out the 10%
cut_off = 1000

ariel_sort_so = ariel.sort_values('Planet Period [days]')
cum_time = []
cum = 0
for index, row in ariel_sort_so.iterrows():
    cum += row['Planet Period [days]']
    cum_time.append(cum)

ariel_sort_so['cumulative days'] = cum_time
ariel_sort_so = ariel_sort_so[ariel_sort_so['cumulative days'] < cut_off]
ariel_sort_so.drop(columns=['Unnamed: 0'])
ariel_sort_so = ariel_sort_so.reset_index(drop=True)
ariel_sort_so.index = ariel_sort_so.index + 1



#sort according to the highest ESM or maybe try with # of terrestrial bins
ariel_sort_ESM = ariel.sort_values(by = 'ESM',ascending=False)
cum_time = []
cum = 0
for index, row in ariel_sort_ESM.iterrows():
    cum += row['Planet Period [days]']
    cum_time.append(cum)

ariel_sort_ESM['cumulative days'] = cum_time
ariel_sort_ESM = ariel_sort_ESM[ariel_sort_ESM['cumulative days'] < cut_off]
ariel_sort_ESM.drop(columns=['Unnamed: 0'])
ariel_sort_ESM = ariel_sort_ESM.reset_index(drop=True)
ariel_sort_ESM.index = ariel_sort_ESM.index + 1

ariel_sort_ESM.to_csv(data_dir + 'ESM_Ariel_sort.csv')


ariel_ESM_100 = ariel_sort_ESM.head(100)

############################################3
ariel_sort_eclipse_num = ariel.sort_values('Tier 3 Eclipses')
cum_time = []
cum = 0
for index, row in ariel_sort_eclipse_num.iterrows():
    cum += row['Planet Period [days]']
    cum_time.append(cum)

ariel_sort_eclipse_num['cumulative days'] = cum_time
ariel_sort_eclipse_num = ariel_sort_eclipse_num[ariel_sort_eclipse_num['cumulative days'] < cut_off]
ariel_sort_eclipse_num.drop(columns=['Unnamed: 0'])
ariel_sort_eclipse_num = ariel_sort_eclipse_num.reset_index(drop=True)
ariel_sort_eclipse_num.index = ariel_sort_eclipse_num.index + 1

ariel_sort_eclipse_num.to_csv(data_dir + 'Eclipse_Cum.csv')

ariel_eclipse_100 = ariel_sort_eclipse_num.head(100)

######################## rank everything based on tier 3 transits

ariel_sort_transit_num = ariel.sort_values('Tier 3 Transits')
ariel_transit_100 = ariel_sort_transit_num.head(100)

