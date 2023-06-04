import matplotlib.pyplot as plt

from phasecurve_plot_cheryl import *

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))
min_, max_ = selected_sample['Planet Radius [Rj]'].min(), selected_sample['Planet Radius [Rj]'].max()

cmap = 'PiYG'
x = selected_sample['Planet Temperature [K]'].values
y = selected_sample['ASM High'].values/selected_sample['ASM Low'].values

print(x, y)

m, b = np.polyfit(x,y,1)
poly1d_fn = np.poly1d([m,b])
print(m, b)

Ariel_target_ASM_Day = ax.scatter(selected_sample['Planet Temperature [K]'], selected_sample['ASM High']/selected_sample['ASM Low'],
                                    alpha=1, s=250, c=selected_sample['Planet Radius [Rj]'], marker="o", edgecolor='black',
                                    zorder=2, cmap = cmap, vmin=min_, vmax=max_
                                    )

plt.plot(x, poly1d_fn(x), '--k')

plt.xticks(rotation=45)

clb = fig.colorbar(Ariel_target_ASM_Day, ax=ax)  
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planet Radius [Rj]',fontsize=16)




plt.grid(True, alpha=0.35)
plt.xlabel("Planet Equilibrium Temperature", fontsize=18)
plt.ylabel("ASM Day to Night Ratio", fontsize=18)
plt.title("Ariel Phase Curve Targets: ASM ratio vs T_eq", fontsize=24)
#plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-PhaseCurve-ASM-ratio.jpg')

plt.show()
plt.close()

## now we convert ASM_day into ASM_night
ariel_sort_ASM['ASM Night'] = \
    ariel_sort_ASM['ASM']/(m*ariel_sort_ASM['Planet Temperature [K]'] + b)

## now we convert ASM_day into ASM_night
ariel_sort_eclipse_num['ASM Night'] = \
    ariel_sort_eclipse_num['ASM']/(m*ariel_sort_eclipse_num['Planet Temperature [K]'] + b)

fig, ax = plt.subplots(figsize=(15, 10))
# plt.figure(figsize=(15,10))

min_, max_ = ariel_sort_eclipse_num['Planet Radius [Rj]'].min(), ariel_sort_eclipse_num['Planet Radius [Rj]'].max()
# cmap='viridis_r'
cmap = 'PiYG'

Ariel_plot = ax.scatter(ariel_sort_eclipse_num.index.tolist(), ariel_sort_eclipse_num['ASM Night'],
                        alpha=0.9, s = 50, c = ariel_sort_eclipse_num['Planet Radius [Rj]'], marker="o",
                        label = "Ariel", zorder = 1)

clb = fig.colorbar(Ariel_plot, ax=ax)  
#clb.ax.set_title('Planetary Equilibrium Temperature [K]', fontweight='bold')
clb.set_label('Planet Radius [Rj]',fontsize=16)

plt.grid(True, alpha=0.35)
plt.xlabel("Planet Rank", fontsize=18)
plt.ylabel("ASM Night", fontsize=18)
plt.title("Ariel Phase Curve Targets - # of Eclipse Ranked", fontsize=24)
plt.yscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir + 'Ariel-PhaseCurve-ASM-Planet-Rank-Night.jpg')

plt.show()