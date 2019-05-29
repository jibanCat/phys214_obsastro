import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.cm import get_cmap
import camb

viridis = get_cmap('viridis')

params = camb.CAMBparams()

# baseline model : default cosmology model
params.set_cosmology(H0=67.4, ombh2=0.02283, omch2=0.122011,
    omk=0, tau=0.0543)
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)

params.set_matter_power(
    redshifts=[5000., 1000., 600., 400., 100., 50., 20., 10., 5., 2., 1., 0.])

results = camb.get_results(params)

kh, zs, pks = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

for i, (z, pk) in enumerate(zip(zs, pks)):
    color = 1 - i / len(zs)

    ax.loglog(kh, pk, 
        label='z = {}'.format(z), color=viridis(color))
    ax.set_xlabel('$kh^{-1} Mpc$')
    ax.set_ylabel('$P_k Mpc^{-3}$')

ax.legend()

plt.tight_layout()

plt.savefig("images/bao.png", format='png', dpi=200)
plt.show()