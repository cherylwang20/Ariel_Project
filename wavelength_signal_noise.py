import numpy as np
import matplotlib.pyplot as plt

from astropy.modeling.models import BlackBody
from astropy import units as u
from astropy.visualization import quantity_support

from function_constants import *

bb = BlackBody(temperature=5778*u.K, scale = 1)

flux = bb(7.5*u.micron)
flux_2 = planck(5778)

print(flux.to(u.W/u.m**2/u.steradian/u.Hz)*c/wav**2)
print(flux)
print(flux_2)

### choose a few targets, 3 - 5 for referencing their change in value based on their ASM ranking.


#### check the two instrument that Ariel have
## AIRS  is  the  Ariel  scientific  instrument providing  low-resolution  spectroscopy  in  two  IR  channels
# (called Channel 0, CH0, for the [1.95-3.90] μm band and Channel 1, CH1, for the [3.90-7.80] μm band).
# NIRSpec (1.10-1.95 μm spectrometer with R ≥ 15)


####