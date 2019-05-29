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
    redshifts=[9, 2, 1])

# setup non-linear
params.NonLinear = camb.model.NonLinear_both

results = camb.get_results(params)

kh, zs, pks = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

fig, ax = plt.subplots(1, 2, figsize=(10, 6))

for i, (z, pk) in enumerate(zip(zs, pks)):
    color = 1 - i / len(zs)

    ax[0].loglog(kh, pk, 
        label='z = {}'.format(z), color=viridis(color))
    ax[0].set_xlabel('$k h / Mpc$')
    ax[0].set_ylabel('$P_k$')

    ax[1].semilogy(2 * np.pi / (kh*0.674), pk, 
        label='z = {}'.format(z), color=viridis(color))
    ax[1].set_xlabel('scale = $2 \pi / k$ Mpc')
    ax[1].set_ylabel('$P_k$')
    ax[1].set_xlim(1, 300)
    
ax[1].vlines(130, 1, 1e4, label="fitted by my eyes")
ax[1].vlines(150, 1, 1e4, label="BAO peak supposed to be here", ls='--')

ax[0].legend()
ax[1].legend()

plt.tight_layout()

plt.savefig("images/bao_129.png", format='png', dpi=200)
plt.show()