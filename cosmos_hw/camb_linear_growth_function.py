import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.cm import get_cmap
import camb 

viridis = get_cmap('viridis')

params = camb.CAMBparams()

# set parameters based on Planck 2018
params.set_cosmology(
    H0=67.4, ombh2=0.022383, omch2=0.122011, 
    omk=0, tau=0.0543)
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)

params.set_matter_power(redshifts=[9., 2., 1., 0.])

# compute linear power spectrum
results   = camb.get_results(params)
kh, zs, pks = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

for i, (z, pk) in enumerate(zip(zs, pks)):
    color = 1 - i / len(zs)

    ax.loglog(kh, pk, 
        label='z = {}'.format(z), color=viridis(color))
    ax.set_xlabel(r'$k h$ $Mpc^{-1}$')
    ax.set_ylabel(r'$P_k$ $h^{-3}Mpc^{3}$')

    if i < len(zs) - 1:
        linear_growth = (pks[i, :] / pks[i + 1, :]).mean()

        print("Linear growth rate between z = {} ~ {} is {}".format(
            zs[i], zs[i + 1], linear_growth
        ))

ax.legend()

plt.savefig("images/linear_growth.png", format="png", dpi=200)
plt.show()

