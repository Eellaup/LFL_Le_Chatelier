#########################################################################
# * Project           : Lower Flammability Limit Calculator for Gas Mixtures
# *
# * Program name      : lfl_calc.py
# *
# * Author            : Paul Lee (plee)
# *
# * Date created      : 20200602
# *
# * Purpose           : Calculate LFL for complex gas mixtures based on Le Chatelier's rule
# *
# * Revision History  :
# *
# * Date        Author      Ref    Revision (Date in YYYYMMDD format)
# * 20200602    plee         1     Created bulk code
# * 20201007    plee         2     Added feature to test if gas is flammable
# *
#########################################################################

# import gas characteriziations
from src.LFL_Calculator import LFL_Calculator
from src.func import *
from src.gas_char import *

def main2():
    # INPUT - GAS CONCENTRATIONS
    inputGas = {'h2':30,'co':5,'ch4': 10,'ar':55}
    inputGas = {'h2':1.509,'co':0.854,'co2':0.000,'ch4':1.060}
    lfl_calc = LFL_Calculator()

    print(lfl_calc.LFL(inputGas))


def main():
    # INPUT - GAS CONCENTRATIONS
    flam_gas_conc = {'h2':30,'co':5,'ch4': 10}
    inert_gas_conc = {'ar':55}

    # print input Gas mixture
    print('\nGas Mixture Input:')
    for gas in flam_gas_conc:
        print('  ', gas, ': ', flam_gas_conc[gas], '%')
    for gas in inert_gas_conc:
        print('  ', gas, ': ', inert_gas_conc[gas], '%')

    # Gas Concentration Checker
    if sum(flam_gas_conc.values()) + sum(inert_gas_conc.values()) != 100:
        print('\nERROR: Gas Concentration Input DOES NOT ADD UP TO A 100%')
    else:
        # LFL Calculation

        # if air is in the input, take it out for the lfl calculation
        if 'air' in inert_gas_conc:
            air_volume = inert_gas_conc['air']
            flam_gas_conc, inert_gas_conc = ratio_no_air(
                flam_gas_conc, inert_gas_conc)

            lfl_mixture = lfl_calc(flam_gas_conc, inert_gas_conc)
        # no air in the input :)
        else:
            air_volume = 0
            lfl_mixture = lfl_calc(flam_gas_conc, inert_gas_conc)

        print('\nRESULT:')
        print('  LFL of Mixture (without air): ',
              round(lfl_mixture, 2), 'mol %')
        print('  Is it higher than LFL?: ', 'YES' if (
            100-air_volume) > lfl_mixture else 'NO')
        print()


if __name__ == '__main__':
    main()
    main2()
