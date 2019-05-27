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

** b) Compare this result to Figure 1 of https://arxiv.org/abs/1807.06209. Do your results look similar?**

Yes.

## Prob 2.3 Baryons in the CMB