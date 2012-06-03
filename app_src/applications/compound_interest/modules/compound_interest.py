'''
Created on 2012-1-1

definition:
http://en.wikipedia.org/wiki/Compound_interest

FV = further value
PV = present value
fi = fixed interest rate
np = number of periods

@author: xiaoftang
'''

def get_further_value(pv, fi, np):
    '''
    get further value
    '''
    return pv * ((1 + fi) ** np)

def get_further_value_per_year(pv_per_year, fi, np):
    '''
    get further value
    '''
    sum = 0
    for i in range(np):
        sum += pv_per_year
        sum = sum * (1 + fi)
    return sum

def get_present_value(fv, fi, np):
    '''
    get present value
    '''
    return fv / ((1 + fi) ** np)

def get_fixed_interest_rate(fv, pv, np):
    '''
    get fixed interest value
    '''
    return (fv / pv) ** (1 / np) - 1

def get_periods(fv, pv, fi):
    '''
    get fixed interest value
    '''
    from math import log
    return log((fv / pv), 1 + fi)

