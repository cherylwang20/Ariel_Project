from phasecurve_plot_cheryl import *

############# we are looking at tier 2 resolution at the moment

ariel = ariel.head(20)

#N_lambda = 75 ## change to different # of bins for different spectrometers?
SNR_thres = 7
start, end = 1.10, 7.8
spectrometer = "All" # "All" or "NIRSpec"or "AIRS-CH0" or "AIRS-CH1",
Tier = 1
mode = "transmission"  # "transmission" or "emission"
if mode == "emission":
    if spectrometer == "NIRSpec":
        start, end = 1.10, 1.95
        if Tier == 2:
            N_lambda = 10
        elif Tier == 3:
            N_lambda = 20
    elif spectrometer == "AIRS-CH0":
        start, end = 1.95, 3.90
        if Tier == 2:
            N_lambda = 50
        elif Tier == 3:
            N_lambda = 100
    elif spectrometer == "AIRS-CH1":
        start = 3.90; end = 7.8;
        if Tier == 2:
            N_lambda = 15
        elif Tier == 3:
            N_lambda = 30
    elif spectrometer == "All":
        if Tier == 1:
            N_lambda = 5
        elif Tier == 2:
            N_lambda = 75
        elif Tier == 3:
            N_lambda = 150
elif mode == "transmission":
    spectrometer = 'Trans'
    if Tier == 1:
        N_lambda = 5
    elif Tier == 2:
        N_lambda = 75
    elif Tier == 3:
        N_lambda = 150



# calculate noise based on the required wavelength bin
spec_wave_range = np.linspace(start, end, N_lambda + 1)
print(spec_wave_range)

## generate intervals and labels
labels = []
intervals = []
interval_size = spec_wave_range[1] - spec_wave_range[0]
current = start
while current < end:
    interval_end = min(current + interval_size, end)
    #print(current)
    intervals.append((current, interval_end))
    labels.append(f'{current:.3f}-{interval_end:.3f}')
    current += interval_size
labels = labels[:-1]
intervals = np.round(intervals, 3)


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
plt.title(f'Ariel Target: Noise vs Wavelength ({spectrometer})',fontsize=24, fontweight='bold')
plt.ylabel('# of Photons',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.show()

### calculate the emission signal as a continuous function, plot to check

ariel_signal_range = np.linspace(start, end, 180)*1e-6

target_emiss = []
all_emiss = []

fig, ax = plt.subplots(figsize=(15, 10))


for i, row in ariel.iterrows():
    target_emiss = []
    for j in ariel_signal_range:
        target_emiss.append(ASM_astropy(row['Planet Radius [Rj]'],row['Star Radius [Rs]'], T_day_eff(row['Star Temperature [K]'],
                                            row['Star Radius [Rs]'], row['Planet Semi-major Axis [m]']),row['Star Temperature [K]'], j))
    plt.plot(ariel_signal_range*10**6, target_emiss, label = row['Planet Name'], linewidth = 3)
    all_emiss.append(target_emiss)

plt.grid(True, alpha=0.35)

plt.title(f'Ariel Target: Emission Signal vs Wavelength ({spectrometer})',fontsize=24, fontweight='bold')
plt.ylabel('Thermal Contrast',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.yscale('log')
#plt.show()
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
#print(transit_snr)

count_trans = np.sum(transit_snr > SNR_thres)

if mode == "transmission":
    print(f"At Tier {Tier}, with instrument {spectrometer}, R = {N_lambda}, the # of targets"
      f" with SNR > {SNR_thres} is {count_trans}.")
elif mode == "emission":
    print(f"At Tier {Tier}, with instrument {spectrometer}, R = {N_lambda}, the # of targets"
      f" with SNR > {SNR_thres} is {count_emiss}.")
