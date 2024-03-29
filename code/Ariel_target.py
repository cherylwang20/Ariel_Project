'''
@author: Huiyi (Cheryl) Wang
August 2023

This document import all the Ariel data from excel and transfer it to df
preparation for phasecurve_cheryl_plot
'''


import numpy as np
import pandas as pd
import os

#we convert the excel to a csv file.

data_dir = os.path.join(os.getcwd(), 'data/')

#read hot jupiter temperature data from Taylor
df_jupiter = pd.read_excel(data_dir + "Taylor_Jupiter_Temp.xlsx")
df_jupiter.to_csv(data_dir + 'Jupiter_Temp.csv')

#read Ariel Data
df = pd.read_excel(data_dir + "Known_T1_10Obs_20220525_edits.xlsx")
column_names = df.columns

new_target = df[df['Planet Period [days]'] < 5]


df.to_csv(data_dir + 'ariel_target.csv')


file_name = os.path.join(data_dir, "All JWST transiting exoplanet observations  (GTO+GO+ERS) - All Transiting Exoplanet Observations.csv")
JWST_Cycle1 = pd.read_csv(file_name,skiprows= 7)

#print(len(JWST_Cycle1['Observation']))

JWST_Phase = JWST_Cycle1[JWST_Cycle1['Observation'] == 'PHASE']

print(f'The total JWST cycle 1 timeframe devoted to Phase Curve Observation is ~{11/141*100:.3f}%')

JWST_Phase_Planet = JWST_Phase['Planet']
