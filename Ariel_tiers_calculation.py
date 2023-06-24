from phasecurve_plot_cheryl import *

############# we are looking at tier 2 resolution at the moment

#N_lambda = 75 ## change to different # of bins for different spectrometers?
SNR_thres = 7
spectrometer = "AIRS-CH1" # "NIRSpec"or "AIRS-CH0" or "AIRS-CH1"
Tier = 2

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
intervals = np.round(intervals[:-1], 3)

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
    plt.xticks(range(len(noise_wave)), labels, fontsize = 10)  # , rotation=45, ha='right')

plt.grid(True, alpha=0.35)
plt.yscale('log')
plt.title('Ariel Target: Noise vs Wavelength',fontsize=24, fontweight='bold')
plt.ylabel('# of Photons',fontsize=18, fontweight='bold')
plt.xlabel(r'$\lambda$ ($\mu$m)',fontsize=18, fontweight='bold')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()


