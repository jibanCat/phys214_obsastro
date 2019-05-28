import os
import numpy as np
import camb
from matplotlib import pyplot as plt

if not os.path.exists("COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt"):
    import urllib.request as request
    request.urlretrieve(
        "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt",
        "COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt"
    )

# setup six init params from the paper
params = camb.CAMBparams() # the obj stores params
params.set_cosmology(
    ombh2=0.022383, omch2=0.122011, 
    thetastar=0.0104, omk=0, tau=0.0543)
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)

params.set_for_lmax(2500, lens_potential_accuracy=0)

# calculate the results of params
results = camb.get_results(
    params)

# get power spec
power_spec = results.get_cmb_power_spectra(
    params, CMB_unit="muK", lmax=2500)

# prepare cls
total_cls          = power_spec['total']
unlensed_total_cls = power_spec['unlensed_scalar']

ls = np.arange(total_cls.shape[0])

fig, ax = plt.subplots(2, 1, figsize = (10, 12))
ax[0].plot(ls, total_cls[:, 0],          color='C0', label='lensed')
ax[0].plot(ls, unlensed_total_cls[:, 0], color='k',  label='unlensed', ls='--')
ax[0].set_title("TT Power Spectrum")
ax[0].set_xlim(0, 2500)
ax[0].set_xlabel(r'$\ell$')
ax[0].set_ylabel(r'$\mathcal{D}^{TT}_\ell$ [$\mu K^2$]')
ax[0].legend()


# Compare this result to Figure 1 of https://arxiv.org/abs/1807.06209.
# get data from planck archive
best_fit_results = np.loadtxt("COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt")

planck_ls  = best_fit_results[:, 0]
planck_cls = best_fit_results[:, 1]

ax[1].plot(ls, total_cls[:, 0], color="C0", label="CAMB")
ax[1].plot(planck_ls, planck_cls, color="C1", label="Planck best-fit", ls='--')
ax[1].set_xlim(0, 2500)
ax[1].set_xlabel(r'$\ell$')
ax[1].set_ylabel(r'$\mathcal{D}^{TT}_\ell$ [$\mu K^2$]')
ax[1].legend()

plt.tight_layout()

plt.savefig("images/power_spec.png", format='png', dpi=200)
plt.show()
