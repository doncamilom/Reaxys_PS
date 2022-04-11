#! /usr/bin/env python3

# This file is to define custom periodic tables. For usage in another script use:
# import TPs
# TP1 = TPs.TP  #Load one of the periodic tables defined here into the variable TP1

TP = {'shape':(7,32),
      'xy':{
        'H': (0,0) ,  
        'He':(0,31),
        'Li': (1,0),
        'Be': (1,1),
        'B': (1,26),
        'C': (1,27),
        'N': (1,28),
        'O': (1,29),
        'F': (1,30),
        'Ne':(1,31), 
        'Na': (2,0),
        'Mg': (2,1),
        'Al':(2,26),
        'Si':(2,27),
        'P': (2,28),
        'S': (2,29),
        'Cl':(2,30),
        'Ar':(2,31),
        'K':  (3,0),
        'Ca': (3,1),
        'Sc':(3,16),
        'Ti':(3,17),
        'V': (3,18),
        'Cr':(3,19),
        'Mn':(3,20),
        'Fe':(3,21),
        'Co':(3,22),
        'Ni':(3,23),
        'Cu':(3,24),
        'Zn':(3,25),
        'Ga':(3,26),
        'Ge':(3,27),
        'As':(3,28),
        'Se':(3,29),
        'Br':(3,30),
        'Kr':(3,31),
        'Rb':(4,0),
        'Sr':(4,1),
        'Y' :(4,16),
        'Zr':(4,17),
        'Nb':(4,18),
        'Mo':(4,19),
        'Tc':(4,20),
        'Ru':(4,21),
        'Rh':(4,22),
        'Pd':(4,23),
        'Ag':(4,24),
        'Cd':(4,25),
        'In':(4,26),
        'Sn':(4,27),
        'Sb':(4,28),
        'Te':(4,29),
        'I': (4,30),
        'Xe':(4,31),
        'Cs':(5,0),
        'Ba':(5,1),
        'La':(5,2),
        'Ce':(5,3),
        'Pr':(5,4),
        'Nd':(5,5),
        'Pm':(5,6),
        'Sm':(5,7),
        'Eu':(5,8),
        'Gd':(5,9),
        'Tb':(5,10),
        'Dy':(5,11),
        'Ho':(5,12),
        'Er':(5,13),
        'Tm':(5,14),
        'Yb':(5,15),
        'Lu':(5,16),
        'Hf':(5,17),
        'Ta':(5,18),
        'W': (5,19),
        'Re':(5,20),
        'Os':(5,21),
        'Ir':(5,22),
        'Pt':(5,23),
        'Au':(5,24),
        'Hg':(5,25),
        'Tl':(5,26),
        'Pb':(5,27),
        'Bi':(5,28),
        'Po':(5,29),
        'At':(5,30),
        'Rn':(5,31),
        'Fr':(6,0),
        'Ra':(6,1),
        'Ac':(6,2),
        'Th':(6,3),
        'Pa':(6,4),
        'U':(6,5),
        'Np':(6,6),
        'Pu':(6,7),
        'Am':(6,8),
        'Cm':(6,9),
        'Bk':(6,10),  
        'Cf':(6,11),
        'Es':(6,12),
        'Fm':(6,13),
        'Md':(6,14),
        'No':(6,15),
        'Lr':(6,16),
        },
    'names':{'H': 'Hydrogen',
             'He': 'Helium',
             'Li': 'Lithium',
             'Be': 'Beryllium',
             'B': 'Boron',
             'C': 'Carbon',
             'N': 'Nitrogen',
             'O': 'Oxygen',
             'F': 'Fluorine',
             'Ne': 'Neon',
             'Na': 'Sodium',
             'Mg': 'Magnesium',
             'Al': 'Aluminium',
             'Si': 'Silicon',
             'P': 'Phosphorus',
             'S': 'Sulfur',
             'Cl': 'Chlorine',
             'Ar': 'Argon',
             'K': 'Potassium',
             'Ca': 'Calcium',
             'Sc': 'Scandium',
             'Ti': 'Titanium',
             'V': 'Vanadium',
             'Cr': 'Chromium',
             'Mn': 'Manganese',
             'Fe': 'Iron',
             'Co': 'Cobalt',
             'Ni': 'Nickel',
             'Cu': 'Copper',
             'Zn': 'Zinc',
             'Ga': 'Gallium',
             'Ge': 'Germanium',
             'As': 'Arsenic',
             'Se': 'Selenium',
             'Br': 'Bromine',
             'Kr': 'Krypton',
             'Rb ': 'Rubidium',
             'Sr': 'Strontium',
             'Y': 'Yttrium',
             'Zr': 'Zirconium',
             'Nb': 'Niobium',
             'Mo': 'Molybdenum',
             'Tc': 'Technetium',
             'Ru': 'Ruthenium',
             'Rh': 'Rhodium',
             'Pd': 'Palladium',
             'Ag': 'Silver',
             'Cd': 'Cadmium',
             'In': 'Indium',
             'Sn': 'Tin',
             'Sb': 'Antimony',
             'Te': 'Tellurium',
             'I': 'Iodine',
             'Xe': 'Xenon',
             'Cs': 'Cesium',
             'Ba': 'Barium',
             'Hf': 'Hafnium',
             'Ta': 'Tantalum',
             'W': 'Tungsten',
             'Re': 'Rhenium',
             'Os': 'Osmium',
             'Ir': 'Iridium',
             'Pt': 'Platinum',
             'Au': 'Gold',
             'Hg': 'Mercury',
             'Tl': 'Thallium',
             'Pb': 'Lead',
             'Bi': 'Bismuth',
             'Po': 'Polonium',
             'At': 'Astatine',
             'Rn': 'Radon',
             'Fr': 'Francium',
             'Ra': 'Radium',
             'Rf': 'Rutherfordium',
             'Db': 'Dubnium',
             'Sg': 'Seaborgium',
             'Bh': 'Bohrium',
             'Hs': 'Hassium',
             'Mt': 'Meitnerium',
             'Ds': 'Darmstadtium',
             'Rg': 'Roentgenium',
             'Cn': 'Copernicium',
             'Nh': 'Nihonium',
             'Fl': 'Flerovium',
             'Mc': 'Moscovium',
             'Lv': 'Livermorium',
             'Ts': 'Tennessine',
             'Og': 'Oganesson',
             'La': 'Lanthanum',
             'Ce': 'Cerium',
             'Pr': 'Praseodymium',
             'Nd': 'Neodymium',
             'Pm': 'Promethium',
             'Sm': 'Samarium',
             'Eu': 'Europium',
             'Gd': 'Gadolinium',
             'Tb': 'Terbium',
             'Dy': 'Dysprosium',
             'Ho': 'Holmium',
             'Er': 'Erbium',
             'Tm': 'Thulium',
             'Yb': 'Ytterbium',
             'Lu': 'Lutetium',
             'Ac': 'Actinium',
             'Th': 'Thorium',
             'Pa': 'Protactinium',
             'U': 'Uranium',
             'Np': 'Neptunium',
             'Pu': 'Plutonium',
             'Am': 'Americium',
             'Cm': 'Curium',
             'Bk': 'Berkelium',
             'Cf': 'Californium',
             'Es': 'Einsteinium',
             'Fm': 'Fermium',
             'Md': 'Mendelevium',
             'No': 'Nobelium',
             'Lr': 'Lawrencium',
             '':''}
}

TPshort = {'shape':(9,18),
      'xy':{
        'H': (0,0) ,  
        'He':(0,17),
        'Li': (1,0),
        'Be': (1,1),
        'B': (1,12),
        'C': (1,13),
        'N': (1,14),
        'O': (1,15),
        'F': (1,16),
        'Ne':(1,17), 
        'Na': (2,0),
        'Mg': (2,1),
        'Al':(2,12),
        'Si':(2,13),
        'P': (2,14),
        'S': (2,15),
        'Cl':(2,16),
        'Ar':(2,17),
        'K':  (3,0),
        'Ca': (3,1),
        'Sc':(3,2),
        'Ti':(3,3),
        'V': (3,4),
        'Cr':(3,5),
        'Mn':(3,6),
        'Fe':(3,7),
        'Co':(3,8),
        'Ni':(3,9),
        'Cu':(3,10),
        'Zn':(3,11),
        'Ga':(3,12),
        'Ge':(3,13),
        'As':(3,14),
        'Se':(3,15),
        'Br':(3,16),
        'Kr':(3,17),
        'Rb':(4,0),
        'Sr':(4,1),
        'Y' :(4,2),
        'Zr':(4,3),
        'Nb':(4,4),
        'Mo':(4,5),
        'Tc':(4,6),
        'Ru':(4,7),
        'Rh':(4,8),
        'Pd':(4,9),
        'Ag':(4,10),
        'Cd':(4,11),
        'In':(4,12),
        'Sn':(4,13),
        'Sb':(4,14),
        'Te':(4,15),
        'I': (4,16),
        'Xe':(4,17),
        'Cs':(5,0),
        'Ba':(5,1),
        'Hf':(5,3),
        'Ta':(5,4),
        'W': (5,5),
        'Re':(5,6),
        'Os':(5,7),
        'Ir':(5,8),
        'Pt':(5,9),
        'Au':(5,10),
        'Hg':(5,11),
        'Tl':(5,12),
        'Pb':(5,13),
        'Bi':(5,14),
        'Po':(5,15),
        'At':(5,16),
        'Rn':(5,17),
        'Fr':(6,0),
        'Ra':(6,1),
        'La':(7,2),
        'Ce':(7,3),
        'Pr':(7,4),
        'Nd':(7,5),
        'Pm':(7,6),
        'Sm':(7,7),
        'Eu':(7,8),
        'Gd':(7,9),
        'Tb':(7,10),
        'Dy':(7,11),
        'Ho':(7,12),
        'Er':(7,13),
        'Tm':(7,14),
        'Yb':(7,15),
        'Lu':(7,16),
        'Ac':(8,2),
        'Th':(8,3),
        'Pa':(8,4),
        'U':(8,5),
        'Np':(8,6),
        'Pu':(8,7),
        'Am':(8,8),
        'Cm':(8,9),
        'Bk':(8,10),  
        'Cf':(8,11),
        'Es':(8,12),
        'Fm':(8,13),
        'Md':(8,14),
        'No':(8,15),
        'Lr':(8,16),
        },
    'names':{'H': 'Hydrogen',
             'He': 'Helium',
             'Li': 'Lithium',
             'Be': 'Beryllium',
             'B': 'Boron',
             'C': 'Carbon',
             'N': 'Nitrogen',
             'O': 'Oxygen',
             'F': 'Fluorine',
             'Ne': 'Neon',
             'Na': 'Sodium',
             'Mg': 'Magnesium',
             'Al': 'Aluminium',
             'Si': 'Silicon',
             'P': 'Phosphorus',
             'S': 'Sulfur',
             'Cl': 'Chlorine',
             'Ar': 'Argon',
             'K': 'Potassium',
             'Ca': 'Calcium',
             'Sc': 'Scandium',
             'Ti': 'Titanium',
             'V': 'Vanadium',
             'Cr': 'Chromium',
             'Mn': 'Manganese',
             'Fe': 'Iron',
             'Co': 'Cobalt',
             'Ni': 'Nickel',
             'Cu': 'Copper',
             'Zn': 'Zinc',
             'Ga': 'Gallium',
             'Ge': 'Germanium',
             'As': 'Arsenic',
             'Se': 'Selenium',
             'Br': 'Bromine',
             'Kr': 'Krypton',
             'Rb ': 'Rubidium',
             'Sr': 'Strontium',
             'Y': 'Yttrium',
             'Zr': 'Zirconium',
             'Nb': 'Niobium',
             'Mo': 'Molybdenum',
             'Tc': 'Technetium',
             'Ru': 'Ruthenium',
             'Rh': 'Rhodium',
             'Pd': 'Palladium',
             'Ag': 'Silver',
             'Cd': 'Cadmium',
             'In': 'Indium',
             'Sn': 'Tin',
             'Sb': 'Antimony',
             'Te': 'Tellurium',
             'I': 'Iodine',
             'Xe': 'Xenon',
             'Cs': 'Cesium',
             'Ba': 'Barium',
             'Hf': 'Hafnium',
             'Ta': 'Tantalum',
             'W': 'Tungsten',
             'Re': 'Rhenium',
             'Os': 'Osmium',
             'Ir': 'Iridium',
             'Pt': 'Platinum',
             'Au': 'Gold',
             'Hg': 'Mercury',
             'Tl': 'Thallium',
             'Pb': 'Lead',
             'Bi': 'Bismuth',
             'Po': 'Polonium',
             'At': 'Astatine',
             'Rn': 'Radon',
             'Fr': 'Francium',
             'Ra': 'Radium',
             'Rf': 'Rutherfordium',
             'Db': 'Dubnium',
             'Sg': 'Seaborgium',
             'Bh': 'Bohrium',
             'Hs': 'Hassium',
             'Mt': 'Meitnerium',
             'Ds': 'Darmstadtium',
             'Rg': 'Roentgenium',
             'Cn': 'Copernicium',
             'Nh': 'Nihonium',
             'Fl': 'Flerovium',
             'Mc': 'Moscovium',
             'Lv': 'Livermorium',
             'Ts': 'Tennessine',
             'Og': 'Oganesson',
             'La': 'Lanthanum',
             'Ce': 'Cerium',
             'Pr': 'Praseodymium',
             'Nd': 'Neodymium',
             'Pm': 'Promethium',
             'Sm': 'Samarium',
             'Eu': 'Europium',
             'Gd': 'Gadolinium',
             'Tb': 'Terbium',
             'Dy': 'Dysprosium',
             'Ho': 'Holmium',
             'Er': 'Erbium',
             'Tm': 'Thulium',
             'Yb': 'Ytterbium',
             'Lu': 'Lutetium',
             'Ac': 'Actinium',
             'Th': 'Thorium',
             'Pa': 'Protactinium',
             'U': 'Uranium',
             'Np': 'Neptunium',
             'Pu': 'Plutonium',
             'Am': 'Americium',
             'Cm': 'Curium',
             'Bk': 'Berkelium',
             'Cf': 'Californium',
             'Es': 'Einsteinium',
             'Fm': 'Fermium',
             'Md': 'Mendelevium',
             'No': 'Nobelium',
             'Lr': 'Lawrencium',
             '':''}
}

