
import tkinter.ttk as ttk



class Convert:

    length = {'m': 1, 'mm': 0.001, 'cm': 0.01, 'dm': 10, 'km': 1000, 'inch': 0.025, 'mile': 1609.34, 'yard': 0.91,
              'ft': 0.3, 'arshin': 0.71, 'fathom': 2.13, 'verst': 1066.8, 'span': 0.18, 'vershok': 0.044}
    square = {'sq. m': 1, 'hectare': 10000, 'sq. cm': 0.0001, 'sq. km': 1000000, 'sotka': 100, 'acr': 4046.86,
              'sq. inch': 0.00065, 'sq. ft': 0.093, 'sq. mile': 2589988.11}
    volume = {'liter': 1, 'ml': 0.001, 'us gallon': 3.79, 'uk gallon': 4.55, 'barrel': 159, 'c. m': 1000,
              'cup': 0.12, 'bucket': 12.3, 'pint': 0.57, 'c. cm': 0.001, 'c. inch': 0.016}
    mass = {'kg': 1, 'pood': 16.38, 'mg': 0.000001, 'gramm': 0.001, 'uk pound': 0.45, 'ru pound': 0.41, 'ton': 1000,
            'centner': 100, 'carat': 0.0002, 'ounce': 0.028}

    def convert_it(self, amount, sector, first, second):
        return amount * sector[first] / sector[second]

    def clicked(self, s, a, tab, one, two):
        ins = self.convert_it(a, s, one, two)
        lbl = ttk.Label(tab, text=ins, width=42)
        lbl.grid(column=1, row=1, padx=10, pady=0)










"""
        measures = {'length': {'m': 1, 'mm': 0.001, 'cm': 0.01, 'dm': 10, 'km': 1000, 'inch': 0.025, 'mile': 1609.34,
                           'yard': 0.91, 'ft': 0.3, 'arshin': 0.71, 'fathom': 2.13, 'verst': 1066.8, 'span': 0.18,
                           'vershok': 0.044},
                'square': {'sq. m': 1, 'hectare': 10000, 'sq. cm': 0.0001, 'sq. km': 1000000, 'sotka': 100,
                           'acr': 4046.86, 'sq. inch': 0.00065, 'sq. ft': 0.093, 'sq. mile': 2589988.11},
                'volume': {'liter': 1, 'ml': 0.001, 'us gallon': 3.79, 'uk gallon': 4.55, 'barrel': 159, 'c. m': 1000,
                           'cup': 0.12, 'bucket': 12.3, 'pint': 0.57, 'c. cm': 0.001, 'c. inch': 0.016},
                'mass': {'kg': 1, 'pood': 16.38, 'mg': 0.000001, 'gramm': 0.001, 'uk pound': 0.45, 'ru pound': 0.41,
                         'ton': 1000, 'centner': 100, 'carat': 0.0002, 'ounce': 0.028}}        
"""
