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
    redshifts=[9, 2, 1, 0])

# setup non-linear
# params.NonLinear = camb.model.NonLinear_both

results = camb.get_results(params)

kh, zs, pks = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

fig, ax = plt.subplots(1, 3, figsize=(16, 9))

for i, (z, pk) in enumerate(zip(zs, pks)):
    color = 1 - i / len(zs)

    ax[0].loglog(kh, pk, 
        label='z = {}'.format(z), color=viridis(color))
    ax[0].set_xlabel(r'k h $Mpc^{-1}$')
    ax[0].set_ylabel(r'$P_k$')

    ax[1].loglog(2 * np.pi / kh, pk * kh**3, 
        label='z = {}'.format(z), color=viridis(color))
    ax[1].set_xlabel(r'scale = $\frac{2 \pi}{k}$ Mpc $h^{-1}$')
    ax[1].set_ylabel(r'$P_k\times k^3$')
    ax[1].set_xlim(10, 200)
    ax[1].set_ylim(1e-2, 1e1)

    # cut off smooth pk
    w         = np.ones(7, 'd')
    pk_smooth = np.convolve(w / w.sum(), pk, mode='same')
    ax[2].plot(2 * np.pi / kh, np.log10( pk / pk_smooth), color=viridis(color), 
        label="z = {}".format(z))
    ax[2].set_ylim(-0.02, 0.02)
    ax[2].set_xlim(10, 200)
    ax[2].set_xlabel(r'scale = $\frac{2 \pi}{k}$ Mpc $h^{-1}$')
    ax[2].set_ylabel(r'$\log_{10} P(k) / P(k){smooth} $')

    # find bao peak at subtracted pk 
    pk_res     = np.log10( pk / pk_smooth)
    real_scale = 2 * np.pi / kh
    bao_inds   = np.where( (real_scale < 120) * (real_scale > 80) )[0]
    bao_scale  = real_scale[bao_inds][pk_res[bao_inds].argmax()]

    print("BAO scale found at np.log10( pk / pk_smooth) is {} for z = {}".format(
        bao_scale, z
    ))

ax[1].vlines(bao_scale, 0.01, 1e4, label="bao scale found by argmax")
ax[1].vlines(100, 0.01, 1e4, label="BAO peak supposed to be here", ls='--')
ax[2].vlines(bao_scale, -1, 1, label="bao scale found by argmax")


ax[0].legend()
ax[1].legend()
ax[2].legend()

plt.tight_layout()

plt.savefig("images/bao_129.png", format='png', dpi=200)
plt.show()