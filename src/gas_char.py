#########################################################################
# * Project           : Lower Flammability Limit Calculator for Gas Mixtures
# *
# * Program name      : gas_char.py
# *
# * Author            : Paul Lee (plee)
# *
# * Date created      : 20200602
# *
# * Purpose           : Store Gas Characteristic Data
# *
# * Revision History  :
# *
# * Date        Author      Ref    Revision (Date in YYYYMMDD format) 
# * 20200602    plee         1     Added initial values for main gases
# * 20200908    plee         2     Updated values based on ISO 10156:2017
# * 20201007    plee         3     Added air composition
# *
#########################################################################

# LFL Data
lfl_data = {
    'h2':4.0,
    'co':10.9,
    'ch4':4.4,
    'c3h8':1.7,
    'c2h6':2.4
}

# Nitrogen Equivalency (ISO 2010)
k_data = {
    'co2':1.5,
    'air':1.0,
    'n2':1.0,
    'he':0.9,
    'ar':0.55,
    'ne':0.7,
    'kr':0.5,
    'xe':0.5,
    'so2':1.5
}

# Air Composition
air_comp = {
    'n2':78,
    'o2':21,
    'ar':1
}