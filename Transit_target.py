from phasecurve_plot_cheryl import *

overlap_target = pd.merge(ariel_transit_100, ariel_eclipse_100, how = "inner", on = ['Planet Name'])
print(overlap_target)