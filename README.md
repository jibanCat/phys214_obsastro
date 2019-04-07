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