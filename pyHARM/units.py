# Tools for converting a set of self-consistent "code" units to CGS units

import numpy as np

cgs = {
    'CL': 2.99792458e10,
    'QE': 4.80320680e-10,
    'EE': 4.80320680e-10,
    'ME': 9.1093826e-28,
    'MP': 1.67262171e-24,
    'MN': 1.67492728e-24,
    'HPL': 6.6260693e-27,
    'HBAR': 1.0545717e-27,
    'KBOL': 1.3806505e-16,
    'GNEWT': 6.6742e-8,
    'SIG': 5.670400e-5,
    'AR': 7.5657e-15,
    'THOMSON': 0.665245873e-24,
    'JY': 1.e-23,
    'PC': 3.085678e18,
    'AU': 1.49597870691e13,
    'MSOLAR': 1.989e33,
    'RSOLAR': 6.96e10,
    'LSOLAR': 3.827e33
}


def get_cgs():
    return cgs


def get_units_M87(M_unit, tp_over_te=3):
    """Get units dict for MBH=6.2e9, i.e. M87
    See get_units
    """
    return get_units(6.2e9, M_unit, tp_over_te)

def get_units_SgrA(M_unit, tp_over_te=3):
    """Get units dict for MBH=6.2e9, i.e. M87
    See get_units
    """
    return get_units(4.14e6, M_unit, tp_over_te)

def get_units(MBH, M_unit, tp_over_te=3, gam=4/3):
    """Get derived units and certain quantities for a system, given a BH mass and accretion density M_unit.
    Note tp_over_te and gam only matter for Thetae_unit
    Also note Mdotedd assumes 10% efficiency
    """
    out = {}
    out['MBH'] = MBH * cgs['MSOLAR']
    out['M_unit'] = M_unit
    out['L_unit'] = L_unit = cgs['GNEWT']*MBH / cgs['CL']**2
    out['T_unit'] = L_unit / cgs['CL']

    out['RHO_unit'] = RHO_unit  = M_unit / (L_unit ** 3)
    out['U_unit'] = RHO_unit * cgs['CL'] ** 2
    out['B_unit'] = cgs['CL'] * np.sqrt(4. * np.pi * RHO_unit)
    out['Ne_unit'] = RHO_unit / (cgs['MP'] + cgs['ME'])

    if tp_over_te is not None:
        out['Thetae_unit'] = (gam - 1.) * cgs['MP'] / cgs['ME'] / (1. + tp_over_te)
    else:
        out['Thetae_unit'] = cgs['MP'] / cgs['ME']

    out['Mdotedd'] = 4.*np.pi * cgs['GNEWT'] * MBH * cgs['MP'] / (0.1 * cgs['CL'] * cgs['THOMSON'])

    # Add constants
    out.update(cgs)

    return out
