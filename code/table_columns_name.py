'''
@author: Huiyi (Cheryl) Wang
August 2023

This code looks at the best in class method when observing all targets for only once
'''


import os.path

import pandas as pd
from function_constants import *
tableName = 'pscomppars'


ariel = pd.read_csv(os.path.join(data_dir,"ariel_target.csv"))
jupiter_temp = pd.read_csv(os.path.join(data_dir,'Jupiter_Temp.csv' ))

columns = [
    "pl_name",
    "hostname",
    "discoverymethod",
    "disc_year",
    "disc_facility",
    "obm_flag",
    "pl_orbper",
    "pl_trandur",
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
    "GJ 367 b",
    "TOI-561 b",
    "TRAPPIST-1 b",
    "TRAPPIST-1 c",
    "TOI-1685 b",
    "K2-22 b",
    "TOI-2445 b"
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

JWST_transit = [
    "L168-9", "HAT-P-14", "WASP-80", "WASP-80", "WASP-69", "GJ-436", "GJ-436",
    "HAT-P-26", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1",
    "HD-189733", "WASP-80", "WASP-80", "WASP-80", "WASP-80", "WASP-69", "WASP-69",
    "WASP-107", "WASP-107", "GJ-436", "GJ-436", "GJ-436-offset", "GJ-436", "GJ-436",
    "GJ-436", "GJ-3470", "GJ-3470", "GJ-1214", "GJ-1214", "WASP-121", "LTT-9779",
    "HATP1", "HAT-P-1", "WASP-52", "WASP-127", "WASP-80", "WASP-107", "WASP-107",
    "WASP-107", "GJ-3470", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1",
    "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "GJ-357", "L-98-59", "L-98-59",
    "LP-791-18", "WASP-52", "L98-59", "WASP-43", "WASP-107", "WASP-52", "HD189733",
    "HD209458", "HD209458", "HD149026", "HD149026", "WASP-19", "WASP-77A", "GJ1132",
    "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1",
    "WASP-107", "HAT-P-12", "HAT-P-12", "HAT-P-12", "HAT-P-26", "HAT-P-26", "HAT-P-26",
    "HAT-P-26", "HAT-P-26", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1",
    "TRAPPIST-1", "WASP-17", "WASP-17", "WASP-17", "WASP-17", "WASP-17", "WASP-17",
    "WASP-17", "WASP-39", "WASP-39", "WASP-39", "WASP-39", "WASP-43", "WASP-18",
    "HAT-P-14", "WASP-18", "HAT-P-14", "WASP-18", "K2-34", "WASP-164", "HD-189733",
    "HD-189733", "HD-189733", "HD-189733", "HD-189733", "WASP-121", "GL486", "GL486",
    "GJ1214", "LHS-3844", "LHS-3844", "LHS-3844", "TOI-421", "TOI-421", "RHO01-CNC",
    "RHO01-CNC", "GJ-4102", "GJ-4102", "GJ-4102", "GJ-4102A", "GJ-4102", "WOLF-437",
    "WOLF-437", "GJ-1132", "GJ-1132", "GJ-1132", "GJ-341", "GJ-341", "GJ-341",
    "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "HD-189733", "HD-80606", "HD-189733",
    "HD-189733", "HD-189733", "HD-134004", "WASP-166", "WASP-166", "55CNC", "55CNC",
    "55CNC", "55CNC", "55CNC", "CD-38-2551", "V-V1298-TAU", "V-V1298-TAU", "NGTS-10",
    "K2-141", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TOI-178",
    "TOI-178", "TOI-178", "TOI-178", "G-268-38", "G-268-38", "K2-141", "WD1856",
    "WD1856", "WD1856", "WD1856", "WD-1856+534-", "K2-18", "K2-18", "K2-18", "K2-18",
    "K2-18", "K2-18", "K2-18", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1",
    "WASP-127", "KEPLER-51", "HD-80606", "HIP67522", "LP-141-14", "CD-45-5378",
    "TOI-260", "TOI-260", "TOI-776", "TOI-776", "TOI-776", "TOI-776", "TOI-562",
    "TOI-836", "TOI-836", "TOI-836", "TOI-134", "TOI-134", "TOI-134", "TOI-455",
    "TOI-175", "TOI-175", "TOI-402", "TOI-402", "TOI-402", "KEPLER-51", "TRAPPIST-1",
    "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1", "TRAPPIST-1",
    "HATS-72", "HATS-72", "HD-209458", "HD-209458", "LTT1445A", "LTT1445A", "LTT1445A",
    "K2-18", "K2-18", "K2-18", "HAT-P-18", "WASP-96", "L-231-32", "TOI-849", "TOI-849",
    "TOI-849", "TOI-2109", "TOI-2109", "TOI-2109", "WASP-39", "HAT-P-1", "HD106315",
    "HAT-P-11", "WASP-121", "TRAPPIST-1", "TRAPPIST-1", "WASP-94A", "TOI-3984",
    "TOI-3984", "TOI-3984", "TOI-3757", "TOI-3757", "HATS-6", "HATS-6", "HATS-75",
    "HATS-75", "HATS-75", "TOI-5293", "TOI-5293", "TOI-3714", "TOI-3714", "TOI-3714",
    "TOI-5205", "TOI-5205", "TOI-5205", "LTT9779", "KEPLER-86", "TOI-1685", "HD-133112",
    "K2-22", "K2-22", "K2-22", "TOI-1130", "TOI-1130", "TOI-1130", "TOI-1130",
    "TOI-1231", "TOI-1231", "TOI-1231", "LTT-3780", "LTT-3780", "LTT-3780", "TOI-1468",
    "TOI-1468", "TOI-1468", "TOI-270", "TOI-270", "WASP-47", "WASP-47", "WASP-69",
    "WASP-69", "GJ-3473", "GJ-3473", "GJ-3473", "GJ-3473", "GJ-357", "HD-260655",
    "HD-260655", "L-98-59", "LHS-1140", "LHS-1140", "LHS-1140", "LHS-1478",
    "LHS-1478", "LTT-3780", "LTT-3780", "TOI-1468", "TOI-1468", "TOI-1468", "L-231-32",
    "L-231-32", "L-231-32", "L-231-32", "TOI-3235", "TOI-5205", "2MASS-J02531581+0003087",
    "TOI-270", "TRES-4", "KELT-7", "NGTS-2", "WASP-15", "HAT-P-30", "TOI-561",
    "L-98-59", "L-98-59", "L-98-59", "KEPLER-12", "KEPLER-12", "WASP-52", "HAT-P-65",
    "HAT-P-65", "LHS3844", "WASP-96", "L98-59", "L98-59", "TOI-1685", "TOI-1685",
    "GJ9827", "GJ9827", "GJ9827", "GJ9827", "GJ3090", "GJ3090", "GJ3090", "GJ3090",
    "TOI-270", "TOI-270", "TOI-270", "TOI-824", "TOI-824", "HAT-P-11", "HAT-P-11",
    "TOI-125", "TOI-125", "TOI-1685", "TOI-1685", "TOI-1685", "TOI-1685", "TOI-1899"
]

