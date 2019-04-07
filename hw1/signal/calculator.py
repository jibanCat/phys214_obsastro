import math as m
import sympy as sp

t = sp.symbols("t") 

# S/N ratio equation
sn = lambda R_s, R_sky, RN, DN, npix, t : R_s * t / ( R_s * t + R_sky * t * npix + RN**2 * npix + DN * t * npix )**(1/2)

def solve_SN_20(R_s, R_sky, RN, DN, npix, t):
    '''
    Parameters
    ----

    R_s   : float, e/s from source
    R_sky : float, e/s/pix from sky
    RN    : float, sqrt(e/s/pix) readout noise  
    DN    : float, e/s dark current noise
    npix  : int, number of pixels
    t     : sympy.symbol, time to solve

    Return:
    t_20  : the time for S/N reach 20
    '''
    expr = sn(R_s, R_sky, RN**(1/2), DN, npix, t)
    return sp.solve(sp.Eq(expr, 20), t)[0] 