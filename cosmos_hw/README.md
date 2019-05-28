# Cosmos Homework 3

## Prob 2.0 : Parameters

Briefly explain the meaning of each of the six base cosmological parameters.

They used flat prior to infer these six base parameters (the following description is according to 2.1 section in the paper):

1. Ωbh² : baryon density of the universe, defined as Ωb = ρb/ρcrit, where ρcrit is critical density. The h here defined as h ≡ H0 / (100 kms⁻¹ Mpc⁻¹).
2. Ωch² : cold dark matter density.
3. 100θMC: an approximation to the observed angular size of the sound horizon at recombination.
4. τ : optical depth at reionization.
5. ln(10¹⁰ As): initial super-horizon amplitude of curvature perturbations (at k = 0.05 Mpc⁻¹).
6. ns : primordial spectral index.

## Prob 2.1 : Install the code

I prefer to use `pipenv`, so build the environment first by:

```
pipenv install numpy scipy matplotlib pylint --dev
```

and then install `CAMB`,

```
pipenv install camb
```

enter the env by,

```
pipenv shell
```

Clone `CLASS`:

```
git clone https://github.com/lesgourg/class_public.git class
```

Try to compile the `CLASS`:

```bash
cd class/
make

# ModuleNotFoundError: No module named 'Cython'
```

I hope they said we need `Cython` before I ran `make`.
Back to install `Cython` to env:

```bash
pipenv install cython

Installing cython…
Adding cython to Pipfile's [packages]…
✔ Installation Succeeded 
Pipfile.lock (f3d047) out of date, updating to (b68964)…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success! 
Updated Pipfile.lock (f3d047)!
Installing dependencies from Pipfile.lock (f3d047)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 19/19 — 00:00:
```

Rerun `make`:

```
cd class/
make clean
make
```

Few warning no errors.

```bash
./class explanatory.ini

# Running CLASS version v2.7.2 ...
# Writing output files in output/explanatory01_... 
```

Try python `import`:

```python
import classy
# and nothing happened
```

Since it sneakly installed the classy package, it's not recorded in `Pipfile`.

## Prob 2.2 Power Spectrum

**a) Write code to generate a theoretical primary CMB temperature power spectrum for a flat universe with the default cosmological parameters.**

Note :  `ns` and `As` in `InitPower.set_params`.

in my `camb_power_spec.py`:

```python
# setup six init params from the paper
params = camb.CAMBparams() # the obj stores params
params.set_cosmology(
    ombh2=0.022383, omch2=0.122011,
    thetastar=0.0104, omk=0, tau=0.0543)
params.InitPower.set_params(
    As=np.exp(3.0448) * 1e-10, ns=0.96605)
```

The code complains about : `camb.baseconfig.CAMBError: Set H0=None when setting theta`  
so I skipped setting H0.

The plot:

![](images/power_spec.png)

**b) Compare this result to Figure 1 of https://arxiv.org/abs/1807.06209. Do your results look similar?**

Yes.

## Prob 2.3 Baryons in the CMB

**a) Increase Ωbh2 , while keeping H0 fixed, so that Ωb changes.**

Result: first peak becomes higher, second & third peak shifts to smaller scales.  

The first peak position is not changed a lot because the universe fixed at flat curvature.  
Since Ωb increases, the sound speed (cs) decreases.
Because l ∝ current horizon / sound speed horizon ∝ 1 / cs  
So that I expected l would increases.
And the result shows l increase a little at first peak and a lot at second and third peak.

![](images/change_baryon.png)

**b) Now, keeping Ωbh2 fixed, set H0 = 75 km/s/Mpc and thus change Ωb.**

```bash
python camb_change_baryon.py
```

![](images/change_H0.png)

As shown in the Fig, increase H0 would shift the peak positions to larger scales.
It makes sense since if the expansion rate is larger than the structure would be larger.

## Prob 2.4 Curvature

**a) Write code to generate a CMB temperature power spectrum for a closed universe with |ΩK| = 0.1.
Keep ΩMh2, H0 and Ωbh2 constant and vary ΩL**

```
python camb_change_curvature.py
```

```python
    params.set_cosmology(
        H0=67.4, ombh2=0.022383,
        omch2=0.122011, omk=omk, tau=0.0543)
    params.InitPower.set_params(
        As=np.exp(3.0448) * 1e-10, ns=0.96605)
```

![](images/change_curvature.png)

![](images/change_curvature_negative.png)

**b) Explain the changes between these two power spectra**

Increase curvature would move peaks to smaller scales.
It makes sense since if the space is more curved then there would be more small scale structures.

Changing dark energy density is equal to changing ΩK to negative so I just plot negative ΩK instead of ΩL.
The reason is that universe would become negative curved if we do not take into account the missing energy- the dark energy.

## Prob 2.5 Massive Neutrinos and the CMB power spectrum

**a) Write code to generate a theoretical primary CMB temperature power spectrum with the default cosmological parameters, but a total neutrino mass (in three neutrino species) of Σm ν = 1 eV.**

Slight modification again,

```python
    # setup six init params from the paper
    params = camb.CAMBparams() # the obj stores params
    params.set_cosmology(
        H0=67.4, ombh2=0.022383,  
        omch2=0.122011, omk=0, tau=0.0543,
        mnu=mnu, neutrino_hierarchy='degenerate')
    params.InitPower.set_params(
        As=np.exp(3.0448) * 1e-10, ns=0.96605)
```

and run (range mν from 0eV ~ 1eV)

```bash
python cmb_change_neutrino.py
```

![](images/change_neutrino.png)

Note:
- normal hierarchy, where m1 < m2 << m3
- inverted hierarchy, where m1 = m2 >> m3
- degenerate, where m1 = m2 = m3

**b) Plot this CMB power spectrum on the same graph as the default power spectrum from Problem 2.2 and explain the differences between them.**

The line with mν = 0 is the default power spectrum.

It seems to shift the power spectrum to larger scales and suppress the amplitude in first peak a little.

Adding more neutrino to universe would shift the matter-radiation equality epoch and would also supress the growth of perturbations.

I think because neutrino would contribute to radiation density.
The matter-radiation equality happens later.
So the general trend of power spectrum shifts to larger scales.

Also, the free-streaming of the neutrino would suppress the growth of the structures in small scales.