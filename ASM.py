import numpy as np
from function_constants import *

# some constants
k_B = 1.380649 * 10**(-23) #SI units
mu = 2.3

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
    b_ratio = planck_peak(T_d, T_d)/planck(T_star, T_d)
    r_ratio = ((7.1492e+7 *Rp)/(6.957e+8*R_star))**2
    return b_ratio*r_ratio


def planck_peak(T, T_d):
    a = 2.0*h*c**2
    peak_wav = 2898/T_d
    b = h*c/(peak_wav*k*T)
    intensity = a/ ( (peak_wav**5) * (np.exp(b) - 1.0) )
    return intensity

