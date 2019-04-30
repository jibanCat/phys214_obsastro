'''
Setup fitting ellipse : phys214 tutorial 2

I must admit I did not write it in a very elegant way
it's messy but it works for now...
'''

import os
from pyraf import iraf
from astropy.io import fits
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import minimize
import pandas as pd

# input images
input_filename = "small.fits"
output_table   = input_filename.replace(".fits", ".tab")
output_bin     = input_filename.replace(".fits", ".bin")
output_cdf     = input_filename.replace(".fits", ".cdf")
model_image    = input_filename.replace(".fits", "_model.fits")
residual_image = input_filename.replace(".fits", "_res.fits")


# import pacakges
iraf.stsdas()
iraf.analysis()
iraf.isophote()


for f in [output_bin, output_cdf, output_table, 
model_image, model_image.replace("model", "model_new_"),
model_image.replace("model", "res")]:
    if os.path.exists(f):
        os.remove(f)

# define parameters for ellipse run
iraf.ellipse.unlearn()

# geompar guess ...
iraf.ellipse.geompar.x0     = 112
iraf.ellipse.geompar.y0     = 115
iraf.ellipse.geompar.ellip0 = 0.06
iraf.ellipse.geompar.pa0    = 60
iraf.ellipse.geompar.sma0   = 40
iraf.ellipse.geompar.step   = 0.01
iraf.ellipse.geompar.linear = False
iraf.ellipse.geompar.recenter = True
# iraf.ellipse.geompar.saveParList(filename="ellipse.par")

# samplepar
iraf.ellipse.samplepar.nclip = 1
iraf.ellipse.samplepar.sdevice = "stdgraph"
# iraf.ellipse.samplepar.saveParList(filename="ellipse.par")

# magpar    : zero point photometry 
iraf.ellipse.magpar.mag0    = 20.3

# ellipse parameters
iraf.ellipse(input=input_filename, output=output_bin)
iraf.tdump(table=output_bin, datafile=output_table, cdfile=output_cdf)

# model image construction
iraf.bmodel.unlearn()
iraf.bmodel(table=output_bin, output=model_image)

# subtraction
image = fits.open(input_filename)[0].data
model = fits.open(model_image)[0].data

fn = lambda x : np.nanmean(
        ( image - x[0] * model - np.nanmedian(image) )**2
        ) 

res = minimize(fn, (0.1,), method="Nelder-Mead")

iraf.imarith.unlearn()
iraf.imarith.operand1 = model_image
iraf.imarith.op       = "*"
iraf.imarith.operand2 = res.x[0]
iraf.imarith.result   = model_image.replace("model", "model_new_")
iraf.imarith()

iraf.imarith.unlearn()
iraf.imarith.operand1 = input_filename
iraf.imarith.operand2 = model_image.replace("model", "model_new_")
iraf.imarith.op       = "-"
iraf.imarith.result   = model_image.replace("model", "res")
iraf.imarith()

# read table
df_tab = pd.read_csv(output_table, delim_whitespace=True, header=0)
cols   = pd.read_csv(output_cdf, delim_whitespace=True, header=-1)
df_tab.columns = cols.loc[:, 0].values

# series of plottings
plt.figure()
plt.errorbar(df_tab.SMA, df_tab.INTENS, yerr=df_tab.INT_ERR)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("SMA")
plt.ylabel("INTENS")
plt.savefig("images/SMA-INTENS-{}.png".format(input_filename.replace(".fits","")))

plt.figure()
plt.errorbar(np.log(df_tab.SMA), df_tab.MAG, yerr=df_tab.MAG_LERR)
plt.xlabel("log(SMA)")
plt.ylabel("MAG")
plt.savefig("images/log(SMA)-MAG-{}.png".format(input_filename.replace(".fits","")))

plt.figure()
plt.errorbar(np.log(df_tab.SMA), df_tab.ELLIP, yerr=df_tab.ELLIP_ERR)
plt.xlabel("log(SMA)")
plt.ylabel("ELLIP")
plt.savefig("images/log(SMA)-ELLIP-{}.png".format(input_filename.replace(".fits","")))

plt.figure()
plt.errorbar(np.log(df_tab.SMA), df_tab.PA, yerr=df_tab.PA_ERR)
plt.xlabel("log(SMA)")
plt.ylabel("PA")
plt.savefig("images/log(SMA)-PA-{}.png".format(input_filename.replace(".fits","")))

plt.figure()
plt.errorbar(df_tab.SMA, df_tab.B4, yerr=df_tab.B4_ERR)
plt.xlabel("SMA")
plt.ylabel("B4")
plt.savefig("images/SMA-B4-{}.png".format(input_filename.replace(".fits","")))
