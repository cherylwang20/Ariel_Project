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

fig, ax = plt.subplots(figsize=(15, 10))
for i, row in targets.iterrows():
    plt.bar(range(len(all_sig[0])), all_sig[i], label = row['Planet Name'] )
plt.xticks(range(len(noise_wave)), labels[:-1])#, rotation=45, ha='right')

plt.grid(True, alpha=0.35)

plt.title('Ariel Target: S/N vs Wavelength',fontsize=24, fontweight='bold')
plt.ylabel('Ariel S/N Metric',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#matplotx.line_labels()
#plt.xscale('log')
#plt.yscale('log')
plt.legend(loc ='upper left')
textstr = f"Average S/N {all_fom} \nAverage Sig/Average Uncer {average_snr}"
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(0.02, 0.95, textstr, fontsize=10, transform=plt.gcf().transFigure, bbox=props)
plt.savefig(save_dir + 'Ariel_SNR_Wavelength.jpg')
plt.show()
plt.close()


