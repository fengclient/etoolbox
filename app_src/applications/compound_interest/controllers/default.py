# compound_interest

def index():
    '''
    compound interest calculator
    '''
    return dict()

def calc():
    from compound_interest import *
    pv = fv = fi = np = ''
    invest_per_year = False
    
    logger.debug("vars: %s", request.vars)
    
    if 'pv' in request.vars and request.vars['pv']:
        pv = float(request.vars['pv'])
    if 'fv' in request.vars and request.vars['fv']:
        fv = float(request.vars['fv'])
    if 'fi' in request.vars and request.vars['fi']:
        fi = float(request.vars['fi'])
    if 'np' in request.vars and request.vars['np']:
        np = int(request.vars['np'])
    if 'invest_per_year' in request.vars and request.vars['invest_per_year']:
        invest_per_year = True
    if pv and fi and np:
        if invest_per_year:
            logging.debug("calc further with per year addition")
            fv = get_further_value_per_year(pv, fi, np)
        else:
            logging.debug("calc further with one-time invest")
            fv = get_further_value(pv, fi, np)
    
    #return (pv, fv, fi, np)
    return fv

