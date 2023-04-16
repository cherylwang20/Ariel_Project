import numpy as np
import pandas as pd

#we convert the excel to a csv file.
df = pd.read_excel("Known_T1_10Obs_20220525_edits.xlsx")
column_names = df.columns

new_target = df[df['Planet Period [days]'] < 5]

df.to_csv('ariel_target.csv')
print(new_target)