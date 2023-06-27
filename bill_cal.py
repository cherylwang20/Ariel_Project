from phasecurve_plot_cheryl import *

BE_table6 = pd.read_csv(os.path.join(data_dir, "Billy_Edward_table_6.csv"))

target_eclipse = BE_table6[BE_table6['Preferred Method'] == 'Eclipse']

target_eclipse_2 = target_eclipse[target_eclipse['Maximum Tier'] >= 2]

print(target_eclipse)
print(target_eclipse_2)

same_target = pd.merge(ariel, BE_table6)

print(len(same_target))

###### calculate the transit signal

tran_sg_all = transit_signal(ariel['Planet Radius [Rj]'], T_day_eff(ariel['Star Temperature [K]'],
                                            ariel['Star Radius [Rs]'], ariel['Planet Semi-major Axis [m]']),
                                            ariel['pl_g'],ariel['Star Radius [Rs]'], 4)

print(tran_sg_all)

print(len(ariel[ariel['Tier 3 Eclipses'] <= 1]))
print(len(ariel[ariel['Tier 3 Transits'] <= 1]))