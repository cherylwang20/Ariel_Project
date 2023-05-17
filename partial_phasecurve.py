from phasecurve_plot_cheryl import *

# we define the angle region when which we need to observe
# before and after the eclipse to account for phase curve offset
angle = [45, 60, 80, 90]

partial_cutoff = 500

# we filter out things that are smaller than 2 days
# and we take a partial curve of all greater than 2 days, with the angle we defined

def new_cum_time(df, angle):

    df['Partial Period [days]'] = df['Planet Period [days]'].apply(lambda x: x if x <=2 else x * angle*2/360)

    cum_time = []
    cum = 0
    for index, row in df.iterrows():
        cum += row['Partial Period [days]']
        cum_time.append(cum)

    df['New Cumulative Days'] = cum_time
    df = df[df['New Cumulative Days'] < partial_cutoff]
    df.drop(columns=['Unnamed: 0'])
    df = df.reset_index(drop=True)
    df.index = df.index + 1

    return df

fig, ax = plt.subplots(figsize=(15, 10))

for i in angle:
    curve_df = new_cum_time(ariel_sort_eclipse_num,i)
    ax.plot(curve_df.index.tolist(), curve_df['New Cumulative Days'].tolist(),
                            alpha=1, linewidth=3, label = f'±{i}°',
                            linestyle='dashdot')

ariel_sort_eclipse_num_2 = ariel_sort_eclipse_num[ariel_sort_eclipse_num['cumulative days'] < partial_cutoff]

Ariel_eclipse = ax.plot(ariel_sort_eclipse_num_2.index.tolist(), ariel_sort_eclipse_num_2['cumulative days'].tolist(),
                        alpha = 1, label = "Full Phase Curve", linewidth= 3,
                       color = 'black')


ax.axhline(120, color='orange', linestyle='solid', linewidth=2, alpha=0.75, zorder = 0)


plt.grid(True, alpha=0.35)
plt.xlabel("# of planets", fontsize=18, fontweight='bold')
plt.ylabel("Cumulative Observational Time [days]", fontsize=18, fontweight='bold')
plt.title("Ariel Partial Phase Curve Cumulative Observational Time", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(title = "Partial Observing Angle (°)")
#plt.yscale('log')
#plt.xscale('log')
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Cul-Eclipse.jpg')

plt.show()