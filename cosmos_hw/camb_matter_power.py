import numpy as np 
import matplotlib.pyplot as plt 
import camb

params = camb.CAMBparams()

# set parameters based on Planck 2018
params.set_cosmology(
    H0=67.4, ombh2=0.022383, omch2=0.122011, 
    omk=0, tau=0.0543)
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)

params.set_matter_power(redshifts=[0.])

# compute linear spectrum
results   = camb.get_results(params)
kh, z, pk = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=1, npoints=200)

# get sigma8
sigma_8 = results.get_sigma8()

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

ax.loglog(kh, pk[0, :], label='linear')
ax.set_title("Matter Power at z = {}".format(z[0]))
ax.set_xlabel(r'$k h$ $Mpc^{-1}$')
ax.set_ylabel(r'$P_k$ $h^{-3}Mpc^{3}$')
ax.legend()

plt.tight_layout()

plt.savefig("images/matter_power.png", format="png", dpi=200)
plt.show()

print("Sigma 8 is {}".format(sigma_8[0]))