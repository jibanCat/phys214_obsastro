# TECHNIQUES OF OBSERVATIONAL ASTRONOMY (Spring-2019) : Assignments

- **INSTRUCTOR**: Gabriela Canalizo (UCR)
- **TEXTBOOKs**: http://www.ncra.tifr.res.in:8081/~yogesh/astrotech1_2015/books.html
- **SOFTWARE**: https://astroconda.readthedocs.io/en/latest/

## HW 1 : Signal to noise

- Detail S/N description: https://www.eso.org/~ohainaut/ccd/sn.html
- WFC3 UVIS Exposure Time Calculator: http://etc.stsci.edu/etc/input/wfc3uvis/imaging/
- S/N function :

```python
sn = lambda R_s, R_sky, RN, DN, npix, t : R_s * t / ( R_s * t + R_sky * t * npix + RN**2 * npix + DN * t * npix )**(1/2)
```

Note:

- Airmass would make the source fainter, not the sky background. (My guess is the magnitude of sky already consider the airmass contribution)
- `npix = π r²`, r is the radius of aperture.

In general,

```bash
# general electron counts
R(m) ∝ 10^( - m / 2.5 );           # e-/s

# airmass makes source fainter
R(m) ∝ 10^( - (m + kX) / 2.5 );    # e-/s

# Poisson noise from source
σ = √( R_s * t + R_sky * t * npix + RN**2 * npix + DN * t * npix ) # e-

# S/N
S/N = R_s * t / σ  # dimension-less
```

## TUTORIAL : IRAF/PyRAF

https://github.com/jibanCat/phys214_obsastro/tree/master/tutorial1/intro