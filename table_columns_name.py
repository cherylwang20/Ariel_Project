import pandas as pd
from function_constants import *
tableName = 'pscomppars'


ariel = pd.read_csv(os.path.join(data_dir,"ariel_target.csv"))

columns = [
    "pl_name",
    "hostname",
    "discoverymethod",
    "disc_year",
    "disc_facility",
    "obm_flag",
    "pl_orbper",
    "pl_orbsmax",
    "pl_radj",
    "pl_bmassj",
    "pl_dens",
    "pl_orbeccen",
    "pl_insol",
    "pl_eqt",
    "st_teff",
    "st_mass",
    "st_rad",
    "st_met",
    "st_lum",
    "st_age",
    "sy_dist",
    "sy_kmag"
]

#long and ugly maybe potential workaround in future?
planetname = (
    "51 Peg b",
    "55 Cnc e",
    "CoRoT-2 b",
    "GJ 436 b",
    "HAT-P-2 b",
    "HAT-P-7 b",
    "HATS-24 b",
    "HD 149026 b",
    "HD 179949 b",
    "HD 189733 b",
    "HD 209458 b",
    "HD 80606 b",
    "KELT-1 b",
    "KELT-9 b",
    "KELT-16 b",
    "KELT-20 b",
    "Kepler-7 b",
    "Kepler-8 b",
    "Kepler-10 b",
    "Kepler-12 b",
    "KOI-13 b",
    "Kepler-41 b",
    "Kepler-76 b",
    "LHS 3844 b",
    "LTT 9779 b",
    "MASCARA-1 b",
    "Qatar-1 b",
    "TOI-519 b",
    "WASP-4 b",
    "WASP-5 b",
    "WASP-12 b",
    "WASP-14 b",
    "WASP-18 b",
    "WASP-19 b",
    "WASP-33 b",
    "WASP-36 b",
    "WASP-43 b",
    "WASP-46 b",
    "WASP-64 b",
    "WASP-76 b",
    "WASP-77 A b",
    "WASP-78 b",
    "WASP-82 b",
    "WASP-100 b",
    "WASP-103 b",
    "WASP-121 b",
    "WASP-142 b",
    "WASP-173 A b",
    "XO-3 b",
    "ups And b",
    "K2-141 b",
    "GJ 1214 b",
    "NGTS-10 b",
    "GJ 367 b"
    #"TOI-193", # add in a JWST target
)

columns_ariel = [
    "Tier 3 Eclipses",
    "Tier 3 Transits",
    "Planet Name",
    "Star Name",
    "Preferred Method",
    "Discovery Year",
    "Planet Period [days]",
    "Transit Duration [s]",
    "Cumulative time (days)",
    "Planet Semi-major Axis [AU]",
    "Planet Radius [Rj]",
    "Planet Mass [Mj]",
    "Eccentricity",
    "Planet Temperature [K]",
    "Star Temperature [K]",
    "Star Mass [Ms]",
    "Star Radius [Rs]",
    "Star Metallicity",
    "Star Age [Gyr]",
    "Star Distance [pc]",
    "Star K Mag",
    "Star Spectral Type",
    "Telescope"
]

planet_ariel = ariel["Planet Name"].tolist()
ariel['Telescope'] = ['Ariel']*len(planet_ariel)




SS_eqt = [279,  # Earth
          122,  # Jupiter
          51]  # Neptune

SS_radj = [1 / 11.2,  # Earth
           1,  # Jupiter
           1 / 2.88]  # Neptune


SS_g = [9.8,  # Earth
        24.8,  # Jupiter
        11.5]  # Neptune

SS_orb = [365.2, # Earth
          4331, #Jupiter
          59800] #Neptune

'''
planet_ariel = (
    "GJ 1214 b",
    "K2-266 b",
    "55 Cnc e",
    "GJ 436 b",
    "GJ 3470 b",
    "HD 189733 b",
    "HD 209458 b",
    "XO-6 b",
    "WASP-77 A b",
    "KELT-7 b",
    "WASP-74 b",
    "XO-3 b",
    "WASP-82 b",
    "WASP-14 b",
    "KELT-14 b"
)
'''