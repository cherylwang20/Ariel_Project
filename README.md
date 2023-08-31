# Ariel_Project
Ariel Summer Project

JWST/Spitzer/Hubble data targets are taken from TESS website https://tess.mit.edu/science/tess-acwg/

table_columns_name.py shows the name/column to import from Ariel Excel spreadsheet as well as observing targets from https://exoplanetarchive.ipac.caltech.edu/TAP. It also lists out all targets of interest to pull from the website

Ariel_target.py imports all Ariel targets and JWST data

function_constants.py gives all constants and functions to calculate based on a given data set

phasecurve_plot_cheryl is the main script that does the following (the first three contributed by Jared Splinter):
1. Import exoplanet data from the exoplanet archive (NOTE: the planet name needs to be EXACT)
2. Sort exoplanets to see if those are targets of either/all of the following three telescopes: Spitzer, Hubble, JWST
3. Calculate ESM & planet gravity of target exoplanets & Ariel

Ariel_tiers_calculation is the main script for computing the AESM and ATSM of all targets. Some suggested improvements for the code are included in the top section of the code.
All scripts starting with JWST plot comparison between JWST and Ariel
All scripts starting with JHS plot comparison between JWST, Hubble, Spitzer, and Ariel.

All figures are output into the folder 'Figure'
All initial data and output data are stored in folder data

The Ariel_project_doc.pdf is a comprehensive review of the current Ariel Phase curve and Transit target selection.

Note: ASM and AESM/ATSM are not the same metric. ASM is a very preliminary metric that is not discussed in the document. Use AESM/ATSM as the final references.

Back-up Codes are those used but not detailed in the document.

New target lists from Billy Edwards' is listed in data/Edwards' Target List
