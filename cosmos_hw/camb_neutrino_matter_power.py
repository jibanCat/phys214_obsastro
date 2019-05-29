import numpy as np
import matplotlib.pyplot as plt
import camb

params = camb.CAMBparams()

omch2 = 0.122011
mnu   = 1        # eV

# baseline scenario : default matter power
params.set_cosmology(
    H0=67.4, ombh2=0.022383, omch2=omch2, 
    omk=0, tau=0.0543)
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)

params.set_matter_power(redshifts=[0.], kmax=1)

results = camb.get_results(params)

kh, z, pk = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

sigma_8 = results.get_sigma8()[0]
print("Default sigma_8 = {}".format(sigma_8))

# first scenario : not change Omega_DM
# set parameters based on Planck 2018
params.set_cosmology(
    H0=67.4, ombh2=0.022383, omch2=omch2, 
    omk=0, tau=0.0543,
    mnu=1, neutrino_hierarchy='degenerate')
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)

params.set_matter_power(redshifts=[0.], kmax=1)

results1 = camb.get_results(params)

kh1, z1, pk1 = results1.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

sigma_8_1 = results1.get_sigma8()[0]
print("Add neutrino, sigma_8 = {}".format(sigma_8_1))

# second scenario : change Omega_DM
# Omega_nu h² = mnu / 93.14
omch2 = omch2 - mnu / 93.14

params.set_cosmology(
    H0=67.4, ombh2=0.022383, omch2=omch2, 
    omk=0, tau=0.0543,
    mnu=1, neutrino_hierarchy='degenerate')
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)

params.set_matter_power(redshifts=[0.], kmax=1)

results2 = camb.get_results(params)

kh2, z2, pk2 = results2.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

sigma_8_2 = results2.get_sigma8()[0]
print("Add neutrino, change Omega_cdm, sigma_8 = {}".format(sigma_8_2))

# plot the difference
fig, ax = plt.subplots(1, 1, figsize=(10, 6))

ax.loglog(kh,  pk[0,  :], label=r'default spectrum', color='k')
ax.loglog(kh1, pk1[0, :], label=r'not change $\Omega_{CDM}$', color='C0')
ax.loglog(kh2, pk2[0, :], label=r'change $\Omega_{CDM} = \Omega_{CDM} - \Omega_{\nu}$', color='C0', ls='--')
ax.set_xlabel(r'$k h$ $Mpc^{-1}$')
ax.set_ylabel(r'$P_k$ $h^{-3}Mpc^{3}$')

ax.legend()

plt.savefig("images/neutrino_matter_power.png", format="png", dpi=200)
plt.show()
