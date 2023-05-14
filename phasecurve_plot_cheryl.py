import os.path

import pyvo
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
from table_columns_name import *
from function_constants import *


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
telescopes = pd.read_csv(os.path.join(data_dir,'pl_telescope.csv'))


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
from sorting_ariel import *

####################### plotting

#from JWST_Phasecurve_Graph import *
#from JWST_Phase_Curve_pg import *
#from JWST_Phasecurve_prj import *
#from JWST_Ariel_Phasecurve_PG_Ecc import *
#from JWST_Ariel_Fig3_PR_PP_PT import *
#from JWST_Ariel_ESM_Period_T import *

#from Ariel_Period_Graph import *i ha
#from Ariel_Cumulative_Period import *
#from Ariel_Temperature_Ecc import *
#from Ariel_ESM_Eclipse_Graph import *
#from Ariel_Ecc_Period import *
#from Ariel_Teq_Rp import *
#from Ariel_Teq_period import *
#from Ariel_ESM_Planet_Rank import *
#from Ariel_num_eclipse_rank import *



