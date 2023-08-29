
'''
@author: Huiyi (Cheryl) Wang
August 2023

The code
1. import JWST, Spitzer, Hubble targets from TAP
2. get their parameters listed in table_columns_name
3. get Ariel data
4. calculate the ESM and planet gravity for all targets
5. rank Ariel targets based on different parameters (e.g. ESM, period, ASM, # of Tier 3 Eclipses)
6. those data will be the bases for other calculations and graphs

'''

import pyvo
from table_columns_name import *
from function_constants import *
import matplotlib.pyplot as plt

service = pyvo.dal.TAPService("https://exoplanetarchive.ipac.caltech.edu/TAP")

query = " ".join((
    f"SELECT {', '.join(columns)}",
    f"FROM {tableName}",
    f"WHERE pl_name in {planetname}"
))

results = service.search(query)


pc_df = results.to_table().to_pandas()
#print(pc_df[pc_df['pl_eqt'].isna() == 1])


#read in csv file, this file tells us whether each object is
#observed in any of the three telescope: Hubble,Spitzer,JWST
telescopes = pd.read_csv(os.path.join(data_dir,'pl_telescope-cycle2.csv'))


pc_telescope = pd.merge(pc_df, telescopes, how='left', left_on='pl_name', right_on='Planet_name')

#Drop useless rows.
pc_telescope = pc_telescope.drop(pc_telescope[(pc_telescope['JWST'] == 'No') & (pc_telescope['Spitzer'] == 'No')  & (pc_telescope['Hubble'] == 'No')].index)

#(pc_telescope.query('pl_orbeccen > 0.09'))

pc_telescope['ESM'] = ESM(1.1*pc_telescope['pl_eqt'], pc_telescope['st_teff'],pc_telescope['pl_radj'] ,pc_telescope['st_rad'],pc_telescope['sy_kmag'])

pc_telescope['pl_g'] = (G*M_jup*pc_telescope['pl_bmassj'])/ ((r_jup*pc_telescope['pl_radj'])**2)


#calculate ESM and planet gravity for all ariel potential targets

ariel['ESM'] = ESM(1.1*ariel['Planet Temperature [K]'], ariel["Star Temperature [K]"], ariel["Planet Radius [Rj]"],
                   ariel["Star Radius [Rs]"], ariel["Star K Mag"])

ariel['pl_g'] = (G*M_jup*ariel["Planet Mass [Mj]"])/ ((r_jup*ariel["Planet Radius [Rj]"])**2)

###############

# calculate the ariel emission metric for all ariel targets
row_list = []

for i, row in ariel.iterrows():
    row_list.append(SNR_Ariel(1/24, row['Star Radius [Rs]'], row['Star Distance [pc]'],
                         row['Star Temperature [K]'],lamb_1_ariel, lamb_2_ariel, row['Planet Radius [Rj]'],
                         row['Planet Temperature [K]'])) #row['Planet Period [days]']
#print(row_list)
ariel['ASM'] = pd.DataFrame(row_list)

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