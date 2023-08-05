from phasecurve_plot_cheryl import *

ariel_target = pd.read_csv(os.path.join(data_dir, 'SNR_all_2.csv'))

ariel_target = ariel_target.sort_values(by = 'Tier2 Transit S/N',ascending=False)