'''
@author: Huiyi (Cheryl) Wang
August 2023

Not a major document
AESM and ATSM calculation document
the bins are NOT equally divided
'''

from phasecurve_plot_cheryl import *

############# we are looking at tier 2 resolution at the moment

#ariel = ariel.head(10)

#N_lambda = 75 ## change to different # of bins for different spectrometers?
SNR_thres = 7
Tier = 2
start_NIR, end_NIR = 1.10, 1.95 #start and end wavelengh for NIRSpec
start_0, end_0 = 1.95, 3.90 #start and end wavelength for AIR-CH0
start_1, end_1 = 3.9, 7.8 #start and end wavelength for AIR-CH1

mode = "transmission"  # "transmission" or "emission"
if Tier == 1:
    lambda_1 = np.linspace(start_NIR, end_NIR, 1)
    lambda_2 = np.linspace(start_0, end_0, 3)
    lambda_3 = np.linspace(start_1, end_1 ,3)
    spec_wave_range = np.concatenate((lambda_1, lambda_2[:-1], lambda_3))
elif Tier == 2:
    lambda_1 = np.linspace(start_NIR, end_NIR, 11)
    lambda_2 = np.linspace(start_0, end_0, 51)
    lambda_3 = np.linspace(start_1, end_1 ,16)
    spec_wave_range = np.concatenate((lambda_1[:-1], lambda_2[:-1], lambda_3))
elif Tier == 3:
    lambda_1 = np.linspace(start_NIR, end_NIR, 21)
    lambda_2 = np.linspace(start_0, end_0, 101)
    lambda_3 = np.linspace(start_1, end_1 ,31)
    spec_wave_range = np.concatenate((lambda_1[:-1], lambda_2[:-1], lambda_3))

print(spec_wave_range)





## generate intervals and labels
labels = []
intervals = []
interval_size = spec_wave_range[1] - spec_wave_range[0]
current = start_NIR

for i in range(len(spec_wave_range)-1):
    intervals.append((spec_wave_range[i], spec_wave_range[i+1]))
    labels.append(f'{spec_wave_range[i]:.3f}-{spec_wave_range[i+1]:.3f}')
intervals = np.round(intervals, 3)


#print(labels)
########## calculate precision and noise plot noise to check
all_noise = []
all_precision = []

fig, ax = plt.subplots(figsize=(15, 10))

for i, row in ariel.iterrows():
    noise_wave = []
    precision = []
    for j in range(len(spec_wave_range) - 1):
        num_p = N_photon(row['Transit Duration [s]'] / daytosec, row['Star Radius [Rs]'], row['Star Distance [pc]'],
                 row['Star Temperature [K]'], spec_wave_range[j]*1e-6, spec_wave_range[j + 1]*1e-6)
        noise_wave.append(num_p)
        precision.append(1/np.sqrt(num_p/2))
    all_noise.append(noise_wave)
    all_precision.append(precision)
    plt.bar(range(len(noise_wave)), noise_wave, align='center', label=row['Planet Name'], alpha=0.7)

    # Set the x-axis tick labels
    if len(labels) != len(noise_wave):
        plt.xticks(range(len(noise_wave)-1), labels, fontsize=10)  # , rotation=45, ha='right')
    else:
        plt.xticks(range(len(noise_wave)), labels, fontsize = 10)  # , rotation=45, ha='right')

plt.grid(True, alpha=0.35)
plt.yscale('log')
plt.title('Ariel Target: Noise vs Wavelength',fontsize=24, fontweight='bold')
plt.ylabel('# of Photons',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()
plt.close()

### calculate the emission signal as a continuous function, plot to check
if Tier == 1:
    ariel_signal_range = np.linspace(start_NIR, end_1, 50) * 1e-6
elif Tier == 2:
    ariel_signal_range = np.linspace(start_NIR, end_1, 180) * 1e-6
elif Tier == 3:
    ariel_signal_range = np.linspace(start_NIR, end_1, 345) * 1e-6

target_emiss = []
all_emiss = []

fig, ax = plt.subplots(figsize=(15, 10))


for i, row in ariel.iterrows():
    target_emiss = []
    for j in ariel_signal_range:
        target_emiss.append(ASM_astropy(row['Planet Radius [Rj]'],row['Star Radius [Rs]'], T_eq(row['Star Temperature [K]'],
                                            row['Star Radius [Rs]'], row['Planet Semi-major Axis [m]']),row['Star Temperature [K]'], j))
    plt.plot(ariel_signal_range*10**6, target_emiss, label = row['Planet Name'], linewidth = 3)
    all_emiss.append(target_emiss)

plt.grid(True, alpha=0.35)

plt.title('Ariel Target: Emission Signal vs Wavelength',fontsize=24, fontweight='bold')
plt.ylabel('Thermal Contrast',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.yscale('log')
plt.show()
plt.close()

######## combine the two to get a SNR for the tier + spectrometer we want

all_target_snr = []

#print(len(intervals))

if len(intervals) != len(all_precision[0]):
    intervals = intervals[:-1]


ariel_wl_sig = np.asarray(ariel_signal_range*1e6)
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
    all_target_snr.append(average_sig)
#print(all_target_snr)
#print(all_precision)
#print(np.mean(all_precision, axis = 1))
all_signal = np.array(all_target_snr)/np.array(all_precision)
all_tier_snr = np.mean(all_signal, axis= 1)
#print(all_tier_snr)

ariel['Tier_SNR'] = all_tier_snr

ariel.to_csv(data_dir + 'SNR_all.csv')
count_emiss = np.sum(all_tier_snr > SNR_thres)




###### calculate the transit signal

ariel['Transit Signal'] = transit_signal(ariel['Planet Radius [Rj]'], T_day_eff(ariel['Star Temperature [K]'],
                                            ariel['Star Radius [Rs]'], ariel['Planet Semi-major Axis [m]']),
                                            ariel['pl_g'],ariel['Star Radius [Rs]'])

#print('ariel transit signal', ariel['Transit Signal'])
#print(ariel['Planet Radius [Rj]'], T_day_eff(ariel['Star Temperature [K]'], ariel['Star Radius [Rs]'], ariel['Planet Semi-major Axis [m]']),
                                            #ariel['pl_g'],ariel['Star Radius [Rs]'])

all_precision_mean = np.mean(all_precision, axis = 1)

##print(ariel['Transit Signal'])

#print(np.array(all_precision_mean))

#print(ariel['Transit Signal'].to_numpy())

transit_snr = ariel['Transit Signal'].to_numpy()/np.array(all_precision_mean)
ariel.to_csv(data_dir + 'SNR_all.csv')
print(transit_snr)

count_trans = np.sum(transit_snr > SNR_thres)


print(f"At Tier {Tier}, the # of targets"
      f" with SNR > {SNR_thres} is {count_trans} in transmission spectroscopy.")

print(f"At Tier {Tier}, the # of targets"
      f" with SNR > {SNR_thres} is {count_emiss} in emission spectroscopy.")
