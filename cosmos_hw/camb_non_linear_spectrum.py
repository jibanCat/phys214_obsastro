import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.cm import get_cmap
import camb

viridis = get_cmap('viridis')

params = camb.CAMBparams()

# set default params based on Planck 2018
params.set_cosmology(
    H0=67.4, ombh2=0.022383, omch2=0.122011, 
    omk=0, tau=0.0543)
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)

params.set_matter_power(redshifts=[9., 2., 1., 0.])

# get linear power spectra
results     = camb.get_results(params)
kh, zs, pks = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

# compute non-linear power spectra
params.NonLinear = camb.model.NonLinear_both
results.calc_power_spectra(params)

kh_nl, zs_nl, pks_nl = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

for i, (z, pk, z_nl, pk_nl) in enumerate(zip(
    zs, pks, zs_nl, pks_nl)):
    
    color = 1 - i / len(zs)

    # plot linear spectrum
    ax.loglog(
        kh, pk, 
        label='z = {} (linear)'.format(z), color=viridis(color))

    # plot non-linear spectrum
    ax.loglog(
        kh_nl, pk_nl, 
        label='z = {} (non-linear)'.format(z_nl), color=viridis(color), 
        ls='--')

ax.set_title('non-linear (dashed) versus linear (solid)')
ax.set_xlabel(r'$k h$ $Mpc^{-1}$')
ax.set_ylabel(r'$P_k$ $h^{-3}Mpc^{3}$')
ax.legend()

plt.tight_layout()

plt.savefig("images/non_linear_matter_power.png", format='png', dpi=200)
plt.show()