'''
print_growth_curve_table.py : load in imexam_*.txt files and 
    print the table of growth curve
'''
import glob
import pandas as pd
from numpy import log, exp, mean
from matplotlib import pyplot as plt

num_radiuses = 10

all_imexam_dfs = [
    pd.read_csv(filename, delim_whitespace=True, escapechar='#') for filename in glob.glob("imexam_*.txt")
]

all_mags = [
    imexam.RMAG.values for imexam in all_imexam_dfs
]

# get the magnitude difference
all_mag_diff = [
    [
        mag1 - mag2 for mag1, mag2 in zip(this_mags, this_mags[1:])
    ]
    for this_mags in all_mags
]

# create growth curve table in pandas form
df = pd.DataFrame(
    all_mag_diff, columns=['radius {}'.format(r) for r in range(2, num_radiuses + 1)])

print("This is the table you want : \n", df)
print("\n")
print("And here is the summary : \n", df.describe())
print("\n")
print("Aperture correction table : \n", df.mean()[::-1].cumsum()[::-1])

plt.plot(df.mean().values)
plt.xticks(range(len(df.mean().index)), df.mean().index, rotation=20)
plt.ylabel("mean( magi - magj )")
plt.savefig("images/mean_mag_diffs.png", format="png", dpi=200)
plt.show()