class LFL_Calculator():
    def __init__(self,verbose: bool = False):
        self.verbose = verbose
    
    # returns the LFL concentration 
    # (Input is dictionary of gas concentrations in vol %)
    # Return in terms of vol %
    def LFL(self, inputGas: dict) -> float:
        # normalize
        inputGas = self.__normalizeGas(inputGas)
        # Categorize input gases
        catGas = self.__categorizeGas(inputGas)
        # sum of gas concentrations
        sumInert = sum(catGas['inert'].values())
        sumFlam = sum(catGas['flam'].values())

        # find lfl of flammable mixture only
        lfl_flam = self.__lfl_flam(catGas['flam'])

        # weighted avg of N2 Equivalency of inert gases
        k_bar = self.__inert_N2Equiv(catGas['inert'])

        # calculate LFL based on Le Chatelier's
        lfl_gas_coeff = ((100-lfl_flam) - (1-k_bar)*(sumInert/sumFlam)*lfl_flam) / (100-lfl_flam)
        lfl_mixture = 0
        for gas,conc in catGas['flam'].items():
            lfl_gas = lfl_gas_coeff * lfl_data.get(gas)
            lfl_mixture += conc / lfl_gas
        lfl_mixture = 100. / lfl_mixture

        return round(lfl_mixture,3)
    
    # normalizes the input gases to sum up to 100%
    def __normalizeGas(self, inputGas: dict) -> dict:
        norm = 100 / sum(inputGas.values())
        inputGas = {k : v * norm for k,v in inputGas.items()}
        return inputGas
    
    # categorize flammable vs inert gas
    def __categorizeGas(self, inputGas: dict) -> dict:
        # initialize
        catGas = {'flam':{}, 'inert':{}}
        # iterate through inputGas
        for gas,conc in inputGas.items():
            # lower case gas
            gas = gas.lower()
            # inert gas
            if gas in k_data: catGas['inert'][gas] = conc
            # flam gas
            elif gas in lfl_data: catGas['flam'][gas] = conc
            # unknown categorization
            else: print('Unknown Categorization: {}'.format(gas))
        return catGas
    
    def __o2_to_air(self,inputGas: dict) -> dict:
        # lower case the keys just in case
        inputGas = {k.lower(): v for k,v in inputGas.items()}
        o2_n2_ratio = 21./79
        # if o2 and n2 are in inputGas
        if 'o2' and 'n2' in inputGas:
            o2 = float(inputGas.get('o2'))
            n2 = float(inputGas.get('n2'))
            # o2 limited
            if (o2/n2) < o2_n2_ratio:
                n2_leftover = n2 - o2 / o2_n2_ratio 
                inputGas.pop
            else:
                o2_leftover = o2 - n2 * o2_n2_ratio
    
    # returns the lfl of the flammable constituents
    def __lfl_flam(self, flamGas: dict) -> float: 
        # initialize lfl of flammable gas
        lfl_flam = 0
        for gas,conc in flamGas.items():
            # Molar fraction of flammable gases
            moleFrac = conc / sum(flamGas.values()) * 100
            # lfl flammable gas
            lfl_flam += moleFrac / lfl_data.get(gas)
        # inverse flammable total
        lfl_flam = 100. / lfl_flam
        return lfl_flam

    # inert gas N2 Equivalency
    def __inert_N2Equiv(self, inertGas: dict) -> float:
        # initialize equivalency factor
        k_bar = 0
        # edge case: no inert gases
        if float(sum(inertGas.values())) == 0:
            return 1
        # weighted sum
        for gas,conc in inertGas.items():
            k_bar += conc * k_data.get(gas)
        # take average
        k_bar /= float(sum(inertGas.values()))
        return k_bar

# Gas Characterization Data

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
    'so2':1.5,
    'o2':1
}

# Air Composition
air_comp = {
    'n2':78,
    'o2':21,
    'ar':1
}