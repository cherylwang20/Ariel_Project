# Ariel_Project
Ariel Summer Project

JWST targets are taken from TESS website https://tess.mit.edu/science/tess-acwg/

table_columns_name.py shows the name/column to import from Ariel excel spreedsheet as well as observing targets from https://exoplanetarchive.ipac.caltech.edu/TAP. It also list out all target of interest to pull from the website

sortin_ariel.py sorts ariel targets based on different requirements

Ariel_target.py imports all ariel targets and JWST data

function_constants.py gives all constant and functions to calculate based on given data set

phasecurve_plot_cheryl is the main script that does the following (first three contributed by Jared Splinter):
1. import exoplanet data from exoplanet achive (NOTE: the planet name needs to be EXACT)
2. sort exoplanet to see if those are targets of either/all the following three telescope: Spitzer, Hubble, JWST
3. calculate ESM & planet gravity of target exoplanets
4. calculate ESM & planet gravity of all ariel targets 
5. plot different scatter/line plots based on data

All figures are output into the folder 'Figure'
All initial data and output data are stored in folder'data'
