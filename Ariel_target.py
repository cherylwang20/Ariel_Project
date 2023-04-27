import numpy as np
import pandas as pd
import os

#we convert the excel to a csv file.
df = pd.read_excel("Known_T1_10Obs_20220525_edits.xlsx")
column_names = df.columns

new_target = df[df['Planet Period [days]'] < 5]
data_dir = os.path.join(os.getcwd(), 'data/')

df.to_csv(data_dir + 'ariel_target.csv')


file_name = os.path.join(data_dir, "All JWST transiting exoplanet observations  (GTO+GO+ERS) - All Transiting Exoplanet Observations.csv")
JWST_Cycle1 = pd.read_csv(file_name,skiprows= 7)

#print(len(JWST_Cycle1['Observation']))

JWST_Phase = JWST_Cycle1[JWST_Cycle1['Observation'] == 'PHASE']
print(JWST_Phase)
print(f'The total JWST cycle 1 timeframe devoted to Phase Curve Observation is ~{11/141*100:.3f}%')

JWST_Phase_Planet = JWST_Phase['Planet']
print(JWST_Phase_Planet)