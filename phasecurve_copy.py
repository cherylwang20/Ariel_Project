import os.path

import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
from table_columns_name import *
from function_constants import *
from ASM import *


#(pc_telescope.query('pl_orbeccen > 0.09'))

#pc_telescope['ESM'] = ESM(1.1*pc_telescope['pl_eqt'], pc_telescope['st_teff'],pc_telescope['pl_radj'] ,pc_telescope['st_rad'],pc_telescope['sy_kmag'])

#pc_telescope['pl_g'] = (G*M_jup*pc_telescope['pl_bmassj'])/ ((r_jup*pc_telescope['pl_radj'])**2)

#calculate ESM and planet gravity for all ariel potential targets

ariel['ESM'] = ESM(1.1*ariel['Planet Temperature [K]'], ariel["Star Temperature [K]"], ariel["Planet Radius [Rj]"],
                   ariel["Star Radius [Rs]"], ariel["Star K Mag"])

ariel['pl_g'] = (G*M_jup*ariel["Planet Mass [Mj]"])/ ((r_jup*ariel["Planet Radius [Rj]"])**2)

# calculate the ariel emission metric for all ariel targets

ariel['ASM'] = ASM(ariel['Planet Radius [Rj]'], ariel['Star Radius [Rs]'], 
                   T_day_eff(ariel['Star Temperature [K]'], ariel['Star Radius [Rs]'], ariel['Planet Semi-major Axis [m]']),
                   ariel['Star Temperature [K]'])

print(ariel['ASM'])

print(ariel)

selected_sample = jupiter_temp.merge(ariel, on='Planet Name',how = 'left')


selected_sample['ESM High'] = ESM(selected_sample['T day (K)'], selected_sample["Star Temperature [K]"], selected_sample["Planet Radius [Rj]"],
                   selected_sample["Star Radius [Rs]"], selected_sample["Star K Mag"])
selected_sample['ESM Low'] = ESM(selected_sample['T night (K)'], selected_sample["Star Temperature [K]"], selected_sample["Planet Radius [Rj]"],
                   selected_sample["Star Radius [Rs]"], selected_sample["Star K Mag"])

selected_sample['ASM High'] = ASM(selected_sample['T day (K)'], selected_sample['Star Radius [Rs]'],
                                  T_day_eff(selected_sample['Star Temperature [K]'], selected_sample['Star Radius [Rs]'], selected_sample['Planet Semi-major Axis [m]'] ),
                                  selected_sample["Star Temperature [K]"])

selected_sample['ASM Low'] = ASM(selected_sample['T night (K)'], selected_sample['Star Radius [Rs]'],
                                  T_day_eff(selected_sample['Star Temperature [K]'], selected_sample['Star Radius [Rs]'], selected_sample['Planet Semi-major Axis [m]'] ),
                                  selected_sample["Star Temperature [K]"])


selected_sample.to_csv(data_dir + 'selected_target.csv')




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
#from Ariel_ESM_diff import *




