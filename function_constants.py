import numpy as np
import os
from scipy.integrate import quad

from astropy.modeling.models import BlackBody
from astropy import units as u

#planck function
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
wav = 7.5e-6 
# g = GM/r^2
G = 6.67e-11
M_jup = 1.89e27
r_jup = 69911*1000
k_B = 1.380649 * 10**(-23) #SI units
mu = 2.3
daytosec = 86400
pctom = 3.086e16


### Ariel Telescope Spec
tau_ariel = 0.3 #system throughput, ****need to check ******
D_ariel = 1 #telescope diameter

## bandpass
lamb_1_ariel = 1.95e-6
lamb_2_ariel = 7.8e-6

save_dir = os.path.join(os.getcwd(),'figure/')
data_dir = os.path.join(os.getcwd(), 'data/')


def planck(T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity

#emission spectroscopy metric (ESM)
def ESM(T_day,T_star, Rp, R_star, mag):
    b_ratio = planck(T_day)/planck(T_star)
    r_ratio = ((7.1492e+7 *Rp)/(6.957e+8*R_star))**2
    mag_ratio = 10**(-mag/5)
    esm = 4.29e6*b_ratio*r_ratio*mag_ratio
    return esm

def ASM(Rp, R_star, T_d, T_star):
    b_ratio = planck_peak(T_d, T_d)/planck_peak(T_star, T_d)
    r_ratio = ((7.1492e+7 *Rp)/(6.957e+8*R_star))**2
    return b_ratio*r_ratio

def ASM_astropy(Rp, R_star, T_d, T_star, wavelength):
    bb_planet = BlackBody(temperature=T_d * u.K, scale=1)
    bb_star = BlackBody(temperature = T_star* u.K, scale=1)

    flux_planet = bb_planet(wavelength * u.m)
    flux_star = bb_star(wavelength * u.m)
    b_ratio = flux_planet/flux_star

    r_ratio = ((7.1492e+7 *Rp)/(6.957e+8*R_star))**2
    return b_ratio.value*r_ratio

def planck_peak(T, T_d):
    a = 2.0*h*c**2
    peak_wav = 2898/T_d*10**(-6)
    b = h*c/(peak_wav*k*T)
    intensity = a/ ( (peak_wav**5) * (np.exp(b) - 1.0) )
    return intensity

# the reflected light constrast ratio
def ref_light(Rp, a, Ag = 0.3):
    return Ag*(Rp/a)**2

# The amplitude of transit spectral features
def transit_signal(Rp, T, g, R_star, N_H = 1):
    H = scale_height(T, g)
    Rp = Rp * 7.1492e+7
    R_star = R_star*6.957e+8
    return 2*Rp*N_H*H/R_star**2

def scale_height(T, g): # T is the dayside effective temperature
    mu = 1.67e-27 * 2
    return k_B*T/mu/g


def N_photon(t, R_star, d, T_star, lamb_1 , lamb_2, tau = tau_ariel, D = D_ariel): #set t to the phase curve period
    B = quad(B_int, lamb_1, lamb_2, args=T_star)
    N = np.pi**2*tau*t*daytosec/h/c*(R_star*6.957e+8*D/2/(d*pctom))**2*B[0]
    wa = (lamb_2 + lamb_1) / 2
    #print(N)
    return N#*wa#**2/c

def B_int(wav, T_star):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T_star)
    intensity = a * wav/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity

def T_day_eff(T_star, R_star, a, A_B = 0.3, eps = 0.2):
    return T_star*np.sqrt(6.957e+8*R_star/a)*(1 - A_B)**0.25*(2/3 - 5*eps/12)**0.25

def SNR_Ariel(t, R_star, d, T_star, lamb_1 , lamb_2, Rp, T_d):
    eps = ASM(Rp, R_star, T_d, T_star)
    n_photon = N_photon(t, R_star, d, T_star, lamb_1 , lamb_2)
    #print(n_photon)
    snr = eps*n_photon/np.sqrt(n_photon)
    return snr

############## partial phase curve
partial_cutoff = 360
def new_cum_time(df, angle):

    df['Partial Period [days]'] = df['Planet Period [days]'].apply(lambda x: x if x <=2 else x * angle*2/360)

    cum_time = []
    cum = 0
    for index, row in df.iterrows():
        cum += row['Partial Period [days]']  + 2 * row['Transit Duration [s]']/ 86400
        cum_time.append(cum)

    df['New Cumulative Days'] = cum_time
    df = df[df['New Cumulative Days'] < partial_cutoff]
    df.drop(columns=['Unnamed: 0'])
    df = df.reset_index(drop=True)
    df.index = df.index + 1

    full_num = len(df[df['Planet Period [days]'] <= 2])
    partial_num = len(df[df['Planet Period [days]'] > 2])
    print(f'{angle}, full num = {full_num}, partial num = {partial_num}')
    return df, full_num, partial_num
