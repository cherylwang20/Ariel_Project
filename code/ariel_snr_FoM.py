'''
@author: Huiyi (Cheryl) Wang
August 2023

The document shows the four example targets final AESM
refer to Figure 7 in Ariel_project_doc.pdf
'''


from ariel_signal_wavelength import *
from Ariel_noise_wavelength import *

print(intervals)
print(target_emiss)

print(intervals[0][1])



all_tg = []
ariel_wl_sig = np.asarray(ariel_wl_sig*1e6)
#print(ariel_wl_sig)
for j in all_emiss:
    average_sig = []
    for i in range(len(intervals)):
        indices = np.where((ariel_wl_sig >= intervals[i][0]) & (ariel_wl_sig <= intervals[i][1]))[0]
        # Retrieve the corresponding y values
        tar_emiss = np.array(j)
        y_within_range = tar_emiss[indices]
        b = np.mean([y_within_range])
        average_sig.append(b)
    #print(len(average_sig))
    all_tg.append(average_sig[:-1])

all_sig  = np.array(all_tg)/np.array(all_precision)
#print(all_sig)
#all_fom = np.sum(all_sig, axis= 1)/(7.8 - 1.1) # per micron
all_fom = np.mean(all_sig, axis=1)
all_fom = np.round(all_fom, 2)
#print(all_fom)#, all_fom_2)

#print(np.array(all_ave)/np.array(all_precision))

############################################### average signal/average noise

#average_noise = np.sum(all_precision, axis = 1)/(7.8 - 1.1)
#average_signal = np.sum(all_tg, axis= 1)/(7.8 - 1.1)

#print(average_signal, average_noise)
#average_snr = average_signal/average_noise

average_snr = np.mean(all_tg, axis= 1)/np.mean(all_precision, axis=1)
average_snr = np.round(average_snr, 2)
#print(average_snr)

print(labels)

mov = [-0.3, -0.1, 0.1, 0.3]

fig, ax = plt.subplots(figsize=(15, 12))
x = np.arange(len(all_precision[0]))
for i, row in targets.iterrows():
    plt.bar(x + mov[i], all_sig[i], width = 0.2,  alpha = 0.7,
            linewidth = 3, label = row['Planet Name'] )
plt.xticks(range(len(noise_wave)), labels[:-1])#, rotation=45, ha='right')

plt.grid(True, alpha=0.35)

#plt.title('Ariel Target: S/N vs Wavelength',fontsize=24, fontweight='bold')
plt.ylabel('Ariel Emission Spectroscopy Metric (AESM)',fontsize=22, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=22, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#matplotx.line_labels()
#plt.xscale('log')
#plt.yscale('log')
handles, plabels = plt.gca().get_legend_handles_labels()

#specify order of items in legend
order = [0, 3, 2, 1]

#add legend to plot
plt.legend([handles[idx] for idx in order],[plabels[idx] for idx in order], loc ='upper left', fontsize = 20)


print(average_snr)
textstr = f"Average S/N {all_fom} \nAverage Sig/Average Uncer {average_snr}"
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#plt.text(0.02, 0.95, textstr, fontsize=10, transform=plt.gcf().transFigure, bbox=props)
plt.savefig(save_dir + 'Ariel_SNR_Wavelength.pdf')
plt.show()
plt.close()


