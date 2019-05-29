import numpy as np
import camb
from matplotlib import pyplot as plt
from matplotlib.cm import get_cmap

viridis = get_cmap("viridis")

def change_lambda(omlambda):
    '''
    omlambda : dark energy density

    other params set to Planck 2018 results
    '''
    H0  = 67.4
    h2  = (H0 * 0.01)**2
    omm = 0.321

    omb = 0.02212 / h2 / (omm + omlambda)
    omc = 0.1206  / h2 / (omm + omlambda) 

    # calc ombh2 and omch2
    ombh2 = omb * h2
    omch2 = omc * h2

    # setup six init params from the paper
    params = camb.CAMBparams() # the obj stores params
    params.set_cosmology(
        H0=H0, ombh2=ombh2, 
        omch2=omch2, omk=0, tau=0.0543)
    params.InitPower.set_params(
        As=np.exp(3.0448) * 1e-10, ns=0.96605)

    params.set_for_lmax(2500, lens_potential_accuracy=0)

    # calculate the results of params
    results = camb.get_results(
        params)

    # get power spec
    power_spec = results.get_cmb_power_spectra(
        params, CMB_unit="muK", lmax=2500)

    return power_spec

# a) Keep ΩMh2, H0 and Ωbh2 constant and vary ΩL.
fig, ax = plt.subplots(1, 1, figsize = (10, 6))

for i in range(11):
    omlambda = 0.679 + i * 0.01

    power_spec = change_lambda(omlambda)
    total_cls          = power_spec['total']
    unlensed_total_cls = power_spec['unlensed_scalar']

    ls = np.arange(total_cls.shape[0])

    ax.plot(ls, unlensed_total_cls[:, 0] , 
        color=viridis( i / 11), label=r'$\Omega_\Lambda = {}$'.format(omlambda))

ax.set_title(r'Change $\Omega_\Lambda$')
ax.set_xlim(0, 2500)
ax.set_xlabel(r'$\ell$')
ax.set_ylabel(r'$\mathcal{D}^{TT}_\ell$ [$\mu K^2$]')
ax.legend()

plt.savefig("images/change_lambda.png", format='png', dpi=200)
plt.show()
