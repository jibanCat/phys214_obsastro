import numpy as np
import camb
from matplotlib import pyplot as plt
from matplotlib.cm import get_cmap

viridis = get_cmap("viridis")

def change_curvature(omk):
    '''
    omk : curvature density

    other params set to Planck 2018 results
    '''
    # setup six init params from the paper
    params = camb.CAMBparams() # the obj stores params
    params.set_cosmology(
        H0=67.4, ombh2=0.022383, 
        omch2=0.122011, omk=omk, tau=0.0543)
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

# a) Keep ΩMh2 , H0 and Ωbh2 constant and vary Ωk
fig, ax = plt.subplots(1, 1, figsize = (10, 6))

for i in range(11):
    omk = 0 + i * 0.01

    power_spec = change_curvature(omk=omk)
    total_cls          = power_spec['total']
    unlensed_total_cls = power_spec['unlensed_scalar']

    ls = np.arange(total_cls.shape[0])

    ax.plot(ls, unlensed_total_cls[:, 0] , 
        color=viridis( i / 11), label=r'$\Omega_k = {}$'.format(omk))

ax.set_title(r'Change $\Omega_k$')
ax.set_xlim(0, 2500)
ax.set_xlabel(r'$\ell$')
ax.set_ylabel(r'$\mathcal{D}^{TT}_\ell$ [$\mu K^2$]')
ax.legend()

plt.savefig("images/change_curvature.png", format='png', dpi=200)
plt.show()

# Keep Ω M h 2 , H 0 and Ω b h 2 constant and vary Ω L .

fig, ax = plt.subplots(1, 1, figsize = (10, 6))

for i in range(11):
    omk = 0 - i * 0.01

    power_spec = change_curvature(omk=omk)
    total_cls          = power_spec['total']
    unlensed_total_cls = power_spec['unlensed_scalar']

    ls = np.arange(total_cls.shape[0])

    ax.plot(ls, unlensed_total_cls[:, 0] , 
        color=viridis( i / 11), label=r'$\Omega_k = {}$'.format(omk))

ax.set_title(r'Change $\Omega_k$')
ax.set_xlim(0, 2500)
ax.set_xlabel(r'$\ell$')
ax.set_ylabel(r'$\mathcal{D}^{TT}_\ell$ [$\mu K^2$]')
ax.legend()

plt.savefig("images/change_curvature_negative.png", format='png', dpi=200)
plt.show()