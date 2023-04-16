import numpy as np
#planck function
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
wav = 7.5e-6 #why this particular wavelength?
# g = GM/r^2
G = 6.67e-11
M_jup = 1.89e27
r_jup = 69911*1000

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