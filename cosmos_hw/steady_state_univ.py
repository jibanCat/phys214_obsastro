import numpy as np 
from scipy.integrate import quad

# physical constants
h = 6.626 * 10**-34         # m^2 kg / s
c = 3 * 10**8               # m / s
k = 1.38 * 10**-23          # m^2 kg s^-2 K^-1

# CMB parameters
nu_max = 5.8 * 10**10 * 2.7 # Hz, from Wien's law
T_cmb  = 2.715
a_f    = (370)**(1/3)       # from (current photon density)^3 / a_f^3 = 1,
                            # this is the estimate of a_f for dropping photo density to 1 photon/cm^3

maxwell_eq = lambda nu, T : 2 * h * nu**3 / c**3 /( np.exp( h * nu / k / T ) - 1)

E_over_the_time =  quad(
    lambda a : maxwell_eq( nu_max * a / a_f, T_cmb * a / a_f ), 1, a_f )[0]

E_null = maxwell_eq(nu_max, T_cmb)

print('''percentage of the energy at the current CMB frequency 
would in fact be from photons created over this time period and 
redshifted from higher frequencies is {} > 1.'''.format(E_over_the_time / E_null))