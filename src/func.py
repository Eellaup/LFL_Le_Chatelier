
# import gas characteriziations
from src.gas_char import *

def ratio_no_air(flam_gas_conc, inert_gas_conc):
    # this takes out air and reconfigures the ratio
    if 'air' in inert_gas_conc:
        for gas in flam_gas_conc:
            flam_gas_conc[gas] = flam_gas_conc[gas] / (100 - inert_gas_conc['air']) * 100
        for gas in inert_gas_conc:
            inert_gas_conc[gas] = inert_gas_conc[gas] / (100 - inert_gas_conc['air']) * 100
        del(inert_gas_conc['air'])

    return flam_gas_conc, inert_gas_conc

def lfl_calc(flam_gas_conc,inert_gas_conc):
    # lfl of flammable mixture only
    lfl_flam = 0
    for gas in flam_gas_conc:
        lfl_flam += (flam_gas_conc[gas]/sum(flam_gas_conc.values())*100)/lfl_data[gas]
    lfl_flam = 100/lfl_flam

    # weighted avg of N2 Equivalency of inert gases
    k_bar = 0
    for gas in inert_gas_conc:
        k_bar += inert_gas_conc[gas] * k_data[gas]
    if k_bar == 0: # in the case there are no inert gases present in the mixture
        k_bar = 1
    else:
        k_bar = k_bar/float(sum(inert_gas_conc.values()))

    # lower flammability limit in mol %
    print('\nLFL of each Gas')
    lfl_mixture = 0
    for gas in flam_gas_conc:
        lfl_gas = ( (100-lfl_flam-(1-k_bar)*(sum(inert_gas_conc.values())/sum(flam_gas_conc.values()))*lfl_flam) / (100 - lfl_flam) ) * lfl_data[gas]
        lfl_mixture += flam_gas_conc[gas] / lfl_gas
        print('  LFL',gas,' :',round(lfl_gas,2),'mol %')
    lfl_mixture = 100 / lfl_mixture

    # Print Results
    print("\nLe Chatelier's Parameters:")
    print('  LFL Flammable Mixture: ',round(lfl_flam,2),'mol %')
    print('  K Bar: ',round(k_bar,2))

    return lfl_mixture