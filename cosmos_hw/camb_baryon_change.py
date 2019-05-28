import numpy as np
import camb
from matplotlib import pyplot as plt
from matplotlib.cm import get_cmap

viridis = get_cmap("viridis")

def change_baryon(ombh2, H0):
    '''
    ombh2 : baryon density
    H0    : current Hubble rate

    other params set to Planck 2018 results
    '''
    # setup six init params from the paper
    params = camb.CAMBparams() # the obj stores params
    params.set_cosmology(
        H0=H0, ombh2=ombh2, 
        omch2=0.122011, omk=0, tau=0.0543)
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

# a) Increase Ω b h 2 , while keeping H 0 fixed, so that Ω b changes.
fig, ax = plt.subplots(1, 1, figsize = (10, 6))

for i in range(10):
    ombh2 = 0.022383 + 0.001 * i

    power_spec = change_baryon(ombh2=ombh2, H0=67.4)
    total_cls          = power_spec['total']
    unlensed_total_cls = power_spec['unlensed_scalar']

    ls = np.arange(total_cls.shape[0])

    ax.plot(ls, unlensed_total_cls[:, 0] , 
        color=viridis( i / 10), label=r'$\Omega_b = {}$'.format(ombh2))

ax.set_title(r'Change $\Omega_b$')
ax.set_xlim(0, 2500)
ax.set_xlabel(r'$\ell$')
ax.set_ylabel(r'$\mathcal{D}^{TT}_\ell$ [$\mu K^2$]')
ax.legend()

plt.savefig("images/change_baryon.png", format='png', dpi=200)
plt.show()

# b) Now, keeping Ωbh2 fixed, set H0 = 75 km/s/Mpc and thus change Ωb

fig, ax = plt.subplots(1, 1, figsize = (10, 6))

for i in range(10):
    H0 = 75 - i * 0.84

    power_spec = change_baryon(ombh2=0.022383, H0=H0)
    total_cls          = power_spec['total']
    unlensed_total_cls = power_spec['unlensed_scalar']

    ls = np.arange(total_cls.shape[0])

    ax.plot(ls, unlensed_total_cls[:, 0] , 
        color=viridis( i / 10), label=r'$H_0 = {}$'.format(H0))

ax.set_title(r'Change $H_0$')
ax.set_xlim(0, 2500)
ax.set_xlabel(r'$\ell$')
ax.set_ylabel(r'$\mathcal{D}^{TT}_\ell$ [$\mu K^2$]')
ax.legend()

plt.savefig("images/change_H0.png", format='png', dpi=200)
plt.show()