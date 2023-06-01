import numpy as np
from function_constants import *
from phasecurve_plot_cheryl import *
from scipy.integrate import quad

# some constants
k_B = 1.380649 * 10**(-23) #SI units
mu = 2.3
daytosec = 86400
pctom = 3.086e16

# the reflected light constrast ratio
def ref_light(Rp, a, Ag = 0.3):
    return Ag*(Rp/a)**2

# The amplitude of transit spectral features
def amp_tran(Rp, H, R_star, N_H = 4):
    return 2*Rp*N_H*H/R_star**2

def scale_height(T, g): # T is the dayside effective temperature
    return k_B*T/mu/g

# Day-side effective temperature
def T_day_eff(T_star, R_star, a, A_B = 0.3, eps = 0.2):
    return T_star*np.sqrt(6.957e+8*R_star/a)*(1 - A_B)**0.25*(2/3 - 5*eps/12)**0.25

# thermal constrast ratio
def ASM(Rp, R_star, T_d, T_star):
    b_ratio = planck_peak(T_d, T_d)/planck_peak(T_star, T_d)
    r_ratio = ((7.1492e+7 *Rp)/(6.957e+8*R_star))**2
    return b_ratio*r_ratio


def planck_peak(T, T_d):
    a = 2.0*h*c**2
    peak_wav = 2898/T_d*10**(-6)
    b = h*c/(peak_wav*k*T)
    intensity = a/ ( (peak_wav**5) * (np.exp(b) - 1.0) )
    return intensity


### Ariel Telescope Spec
tau_ariel = 0.3 #system throughput, ****need to check ******
D_ariel = 1 #telescope diameter

## bandpass
lamb_1_ariel = 1.95e-6
lamb_2_ariel = 7.8e-6

def N_photon(t, R_star, d, T_star, lamb_1 , lamb_2, tau = tau_ariel, D = D_ariel): #set t to the phase curve period
    B = quad(B_int, lamb_1, lamb_2, args=T_star)
    N = np.pi*tau*t*daytosec/h/c*(R_star*6.957e+8*D/2/(d*pctom))**2*B[0]
    return N

def B_int(wav, T_star):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T_star)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity


def SNR_Ariel(t, R_star, d, T_star, lamb_1 , lamb_2, Rp, T_d):
    eps = ASM(Rp, R_star, T_d, T_star)
    n_photon = N_photon(t, R_star, d, T_star, lamb_1 , lamb_2)
    snr = eps*n_photon/np.sqrt(n_photon)
    return snr

e1 = ASM(0.24, 0.7, 619, 5000)
#print(ASM(0.24, 0.2, 619, 3000))
#print(T_day_eff(5000, 0.75, 5*6.957e+8))

n1 = N_photon( 2.5, 0.7,  100, 5000, lamb_1_ariel, lamb_2_ariel)

print('snr', e1*n1/np.sqrt(n1))

print(SNR_Ariel(2.5, 0.7, 100, 5000, lamb_1_ariel, lamb_2_ariel, 0.24, 619))


# calculate the ariel emission metric for all ariel targets
row_list = []

for i, row in ariel.iterrows():
    row_list.append(SNR_Ariel(1/24, row['Star Radius [Rs]'], row['Star Distance [pc]'],
                         row['Star Temperature [K]'],lamb_1_ariel, lamb_2_ariel, row['Planet Radius [Rj]'],
                         row['Planet Temperature [K]'])) #row['Planet Period [days]']
#print(row_list)
ariel['ASM'] = pd.DataFrame(row_list)



#sort according to the highest ASM and see if this matches with the highest # of bins. 
ariel_sort_ASM = ariel.sort_values(by = 'ASM',ascending=False)
cum_time = []
cum = 0
for index, row in ariel_sort_ASM.iterrows():
    cum += row['Planet Period [days]']
    cum_time.append(cum)

ariel_sort_ASM['cumulative days'] = cum_time
ariel_sort_ASM = ariel_sort_ASM[ariel_sort_ASM['cumulative days'] < cut_off]
ariel_sort_ASM.drop(columns=['Unnamed: 0'])
ariel_sort_ASM = ariel_sort_ASM.reset_index(drop=True)
ariel_sort_ASM.index = ariel_sort_ASM.index + 1

ariel_sort_ASM.to_csv(data_dir + 'ASM_Ariel_sort.csv')

fig, ax = plt.subplots(figsize=(15, 10))

Ariel_ASM = ax.scatter(ariel_sort_ASM['ASM'].head(400), ariel_sort_ASM['Tier 3 Eclipses'].head(400), 
                        alpha = 1, linewidth= 3,
                        linestyle = 'dashdot', color = 'red')


plt.grid(True, alpha=0.35)
plt.ylabel("# of Tier 3 Eclipses", fontsize=18, fontweight='bold')
plt.xlabel("ASM", fontsize=18, fontweight='bold')
plt.title("Ariel Phase Curve Comparison of SNR", fontsize=24, fontweight='bold')
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.yscale('log')
plt.xscale('log')
plt.gca().invert_xaxis()
# plt.ylim([0,105])
plt.savefig(save_dir+'Ariel-Phasecurves-Compare.jpg')

plt.show()
