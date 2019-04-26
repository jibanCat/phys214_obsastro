# Phys 214 HW 2

I will be using the web version of `iObserve` in this homework, it's called https://www.arcsecond.io/iobserve. It's currently in beta version.  
I haven't used `iObserve` before, but I heard it's a very handy app because it includes : airmass charts, finding chart, night log, and also connect to other oneline catalogue database.

## Targets:

```cs
# all targets
   targets,                     RA,             DEC,
1. RIXOS F236_021,              17h 00m 35.8s,  51:48:30
2. PG1404+226,                  14h 06m 21.91s, 22:23:46.2
3. SDSS J125603.52+275506.5,    12h 56m 03.52s, 27:55:06.5
4. 3C 319,                      15h 24m 5.60s,  54:28:18.4
5. 2MASX J15335467+2356150,     15h 33m 54.68s, 23:56:14.7
6. Mrk 877,                     16h 20m 11.28s, 17:24:27.5
7. Hercules A,                  16h 51m 8.02s,   4:59:34.9
8. Mrk 728,                     11h  1m 1.77s,  11:02:48.9
9. MCG+04-22-042,                9h 23m 43.0s,  22:54:32.6
10. RBS 1303,                   13h 41m 12.88s,-14:38:40.2
```

## (a) The best one night could observe all targets

Mar 22 - 26 2020 would be good enough based on local mean sidereal time.

Reason:
We need to consider a date the would include the RAs of all targets (consider RA to be an approximated time that the target would show up).  
The RAs of our targets range from 9h to 17 hr.  
Current date, Apr 26 2019, is approximated (365 * 19 + 4 * 30 + 26) days away from Jan 1 2000.
There would be 1 / 15 hour offset from sidereal time for each day.
So the offset of hours at Apr 26 is around (365 * 19 + 4 * 30 + 26) * 15 % 24 ~ 16 hour.  
It means the conversion from LMST 9h to local time is 17h.  
The desired time is around two or three hours later than 17h local time.  
So the sidereal time should be lower for around two or three hours.  
Convert to days, (2 or 3) * 15 ~ (30 or 45) days, which means it's around one month earlier next year.  
So Mar 26 would be good enough.  
After checking with iObserve, Mar 22-26 2020 would be the ideal week.

## (b) Assume that you have been granted one night during the week that you requested, so now you have to prepare for your run. Print an airmass chart for all the targets during that night

See the pic.

![](https://i.imgur.com/tdO4Ziy.png)
Air mass chart is on the left hand side, shaded area is the airmass threshold ~ 3.  
White line is moon.  
Orange lines are targets.  
X-axis is local time.

![](https://i.imgur.com/05SCnFf.png)
![](https://i.imgur.com/QaYz14a.png)

## (c) Print (well, save to a PDF file) a 10’x10’ finderchart for each of the targets. Most guide cameras have CCDs that are more sensitive in the red (about R band), so choose the filter for your finder charts accordingly. Make sure that your target is clearly visible in your finderchart. If there are several targets near the center, mark your target. If your target is not visible, make sure you indicate the spot where your target should be. You can use DSS or SDSS or any of the tools available at the Keck website

Open the Aladin View in iObserve: Filter-- select DSS2 RED

- RIXO F236_021 : not easy to find
![](https://i.imgur.com/CvL6oHb.png)

- PG1404+226 :
![](https://i.imgur.com/Q9YRZK0.jpg)

- SDSS J125603.52+275506.5 (No FinderChart in iObserve) 
![](https://i.imgur.com/FBz0Xe5.png)

- 3C 319 : 3 objects aligned
![](https://i.imgur.com/VDIqmFX.jpg)

- Mrk 877 :
![](https://i.imgur.com/a9Em1v6.jpg)

- Hercules A : crowded
![](https://i.imgur.com/bn14ixk.jpg)

- Mrk 728 :
![](https://i.imgur.com/SRQpQul.jpg)

- MCG+04-22-042 : one object nearby connected to it
![](https://i.imgur.com/E9MsfHE.jpg)

- RBS 1303 :
![](https://i.imgur.com/rdJyExN.jpg)

Oh no, I forgot to fix the size to 10'x10'.

## (d) Choose three spectrophotometric standards that you can observe during the night. Choose them so that they will fit better in your overall plan (later in the quarter we will learn how to pick stars that are better suited for your observations). Avoid stars brighter than about R = 7 (they may saturate too quickly) or fainter than R=14 (you want to get lots of photons in a short time). You can choose them from this list: http://www2.keck.hawaii.edu/inst/common/flux_stds.html Note that if standard stars are bright, you can observe them during twilight

I think ~1 to ~1.5 hour earlier than the earliest target would be fine with we want to observe it during twilight. Potential standards selected from RA are:

```cs
targets,       RA,            DEC,           R
L745-46A,      07:40:19.6,	-17:24:42,   12.9
G193-74,       07:53:27.4,	+52:29:36,   15.5
BD+75° 325,    08:10:49.3,	+74:57:57,    9.7
BD+08° 2015,   08:15:42.4,	+07:37:14,   10.1
PG 0823+546,   08:26:50.4,	+54:28:05.6, 14.63
LTT 3218,      08:41:33.6,	-32:56:54,   12.3
```

The changes of altitudes of standards look like this (via iObserve),
![standards](https://i.imgur.com/ylBkdOt.png)

Discard those standards with R < 14 and choose as bright as possible.
The best choice of mine is `BD+08° 2015`, the reasons are,

- It's bright (R = 10.1) so we may observe during twilight
- The DEC is similar to other targets, so I think it's less effort for telescope to point to the next target

The other two could be, `BD+75° 325` and `L745-46A`.  

- `BD+75° 325` is not as high as `BD+08° 2015` in the sense of altitude, but it's bright enough.  
- `L745-46A` is not as bright as the others, but the altitude is in the middle between the other two.
So it could be a backup if the telescope has some troubles to get too low or too high.

Here is the plot of standards,

```cs
# selected standards
targets,       RA,            DEC,           R
L745-46A,      07:40:19.6,	-17:24:42,   12.9
BD+75° 325,    08:10:49.3,	+74:57:57,    9.7
BD+08° 2015,   08:15:42.4,	+07:37:14,   10.1
```

![standards_plot](https://i.imgur.com/VRQwFOU.png)

The new plot of all targets including the spectrophotometric standards is,
![plotall](https://i.imgur.com/VNsn5eG.png)

## (e) Create a starlist in the format required by Keck. Please pay attention to the details of the format that is required: http://www2.keck.hawaii.edu/inst/common/starlist.html For targets that are hard to see in the findercharts, include also the coordinates of a brighter nearby star or galaxy, and the offsets in RA and DEC using the appropriate keywords

```cs
# all targets
RIXOS F236_021               17 00 35.80  51 48 30.0
PG1404+226                   14 06 21.91  22 23 46.2
3C 319                       15 24 05.60  54 28 18.4
SDSS J125603.52+275506.5     12 56 03.52  27 55 06.5
2MASX J15335467+2356150      15 33 54.68  23 56 14.7
Mrk 877                      16 20 11.28  17 24 27.5
Hercules A                   16 51 08.02  04 59 34.9
Mrk 728                      11 01 01.77  11 02 48.9
MCG+04-22-042                09 23 43.00  22 54 32.6
RBS 1303                     13 41 12.88 -14 38 40.2

# crowded area should include nearby sources
```

I feel some people may have a better way to automate this thing, but I tried in this way:  
`astroquery.ned` 👉  
specify objects in nearby region with some radius 👉  
extract RA/DEC attributes from `astroquery.table.table.Table` class 👉  
convert RA/DEC to proper unit (hh:mm:ss deg:arcmin:arcsec) 👉  
string methods to convert to Keck starlist format.

A small function handles the starlist format for nearby sources,

```python
def nearby2starlist(target_list, radius=30, equinox=2000):
    '''
    query targets in a list and search nearby objects
    print in Keck's starlist format

    Parameters:
    ----
    target_list (list)  : a list of strings include the targets you want to search
    radius      (float) : the radius (in arcmin) you would like to search in nearby

    Returns:
    ----
    starlist    (str)   : Keck style starlist for nearby objects
    '''
    starlist = []
    for target_name in target_list:
        region = Ned.query_region(target_name, radius=radius * u.arcsec)

        all_ras       = region.as_array().data["RA"]
        all_decs      = region.as_array().data["DEC"]
        all_obj_names = region.as_array().data["Object Name"]

        # exclude the target
        ind = ( region.as_array().data["Separation"] != 0 )

        target_ra     = all_ras[~ind][0]
        target_dec    = all_decs[~ind][0]
        target_obj_name = all_obj_names[~ind][0]

        all_ras       = all_ras[ind]
        all_decs      = all_decs[ind]
        all_obj_names = all_obj_names[ind]

        # convert deg to hh:mm:ss
        all_ras_hrs   = [ deg2RA(deg) for deg in all_ras ]
        all_dec_segs  = [ deg2deg_arcmin_arcsec(deg) for deg in all_decs ]

        all_raoffsets  = deg2arcsec(all_ras  - target_ra)      # in arcsec
        all_decoffsets = deg2arcsec(all_decs - target_dec)     # in arcsec  

        # str methods to combine all info to a starlist
        this_starlist = ["# science target {} with nearby offset stars".format(target_name)]
        for ra_hrs, dec_segs, obj_name, raoffset, decoffset in zip(all_ras_hrs, all_dec_segs, all_obj_names, all_raoffsets, all_decoffsets):
            row_str = "{:<30} {:02d} {:02d} {:05.2f}  {:02d} {:02d} {:05.2f}  {:.1f} raoffset={:05.2f} decoffset={:05.2f}".format(
                obj_name.decode("UTF-8"), ra_hrs[0], ra_hrs[1], ra_hrs[2], dec_segs[0], dec_segs[1], dec_segs[2],
                equinox, raoffset, decoffset
            )
            this_starlist.append(row_str)

        starlist.append("\n".join(this_starlist))

        print("\n".join(this_starlist))
        print("\n")


    return starlist
```

```python
from starlist.calc_time import nearby2starlist

target_list = ["RIXOS F236_021", "3C 319", "Hercules A", "Mrk 728", "MCG+04-22-042"]

starlist = nearby2starlist(target_list, radius=30, equinox=2000)
```

the output is,

```cs
# science target RIXOS F236_021 with nearby offset stars
2MASS J17003334+5148150        17 00 33.35  51 48 15.05  2000.0 raoffset=-42.34 decoffset=-11.56


# science target 3C 319 with nearby offset stars
SDSS J152402.37+542815.6       15 24 02.37  54 28 15.67  2000.0 raoffset=-49.00 decoffset=-2.74
[VFK2015] J231.01678+54.46757  15 24 04.03  54 28 03.25  2000.0 raoffset=-24.19 decoffset=-15.16
2MASS J15240491+5428057        15 24 04.91  54 28 05.34  2000.0 raoffset=-10.91 decoffset=-13.07
SDSS J152405.15+542829.3       15 24 05.15  54 28 29.39  2000.0 raoffset=-7.34 decoffset=10.98
SDSS J152405.72+542814.3       15 24 05.72  54 28 14.38  2000.0 raoffset=01.26 decoffset=-4.03
3C 319:[KM95] G1               15 24 05.78  54 28 14.52  2000.0 raoffset=02.12 decoffset=-3.89
SDSS J152406.04+542801.4       15 24 06.05  54 28 01.45  2000.0 raoffset=06.08 decoffset=-16.96
SDSS J152406.44+542750.8       15 24 06.45  54 27 50.80  2000.0 raoffset=12.13 decoffset=-27.61
3C 319:[KM95] G2               15 24 06.67  54 28 19.60  2000.0 raoffset=15.52 decoffset=01.19
SDSS J152406.67+542819.1       15 24 06.68  54 28 19.20  2000.0 raoffset=15.59 decoffset=00.79
SDSS J152406.93+542805.7       15 24 06.94  54 28 05.74  2000.0 raoffset=19.48 decoffset=-12.67


# science target Hercules A with nearby offset stars
SSTSL2 J165106.93+045912.7     16 51 06.93  04 59 12.70  2000.0 raoffset=-18.25 decoffset=-20.63
SSTSL2 J165106.99+045938.2     16 51 06.99  04 59 38.29  2000.0 raoffset=-17.32 decoffset=04.97
GALEXMSC J165107.19+045931.3   16 51 07.20  04 59 31.31  2000.0 raoffset=-14.29 decoffset=-2.02
SSTSL2 J165107.59+045920.3     16 51 07.59  04 59 20.36  2000.0 raoffset=-8.35 decoffset=-12.96
1WGA J1651.1+0459              16 51 07.70  04 59 33.00  2000.0 raoffset=-6.73 decoffset=-0.32
SSTSL2 J165107.86+045913.2     16 51 07.86  04 59 13.27  2000.0 raoffset=-4.32 decoffset=-20.05
HERCULES A Second Nucleus      16 51 07.98  04 59 35.59  2000.0 raoffset=-2.52 decoffset=02.27
SSTSL2 J165107.98+045910.3     16 51 07.99  04 59 10.32  2000.0 raoffset=-2.38 decoffset=-23.00
SSTSL2 J165108.03+045916.6     16 51 08.04  04 59 16.62  2000.0 raoffset=-1.62 decoffset=-16.70
Hercules A Cluster             16 51 08.16  04 59 32.42  2000.0 raoffset=00.18 decoffset=-0.90
SSTSL2 J165108.86+045918.5     16 51 08.87  04 59 18.56  2000.0 raoffset=10.80 decoffset=-14.76
SSTSL2 J165109.08+045938.0     16 51 09.08  04 59 38.08  2000.0 raoffset=14.04 decoffset=04.75
SSTSL2 J165109.09+045908.4     16 51 09.09  04 59 08.41  2000.0 raoffset=14.18 decoffset=-24.91
SSTSL2 J165109.23+045930.6     16 51 09.23  04 59 30.66  2000.0 raoffset=16.27 decoffset=-2.66
SSTSL2 J165109.36+045921.2     16 51 09.37  04 59 21.19  2000.0 raoffset=18.29 decoffset=-12.13
2MASS J16510949+0459536        16 51 09.51  04 59 53.74  2000.0 raoffset=20.41 decoffset=20.41
SSTSL2 J165109.60+045931.1     16 51 09.60  04 59 31.16  2000.0 raoffset=21.85 decoffset=-2.16
SSTSL2 J165109.74+045932.4     16 51 09.74  04 59 32.39  2000.0 raoffset=23.94 decoffset=-0.94
SSTSL2 J165109.86+045926.9     16 51 09.86  04 59 26.92  2000.0 raoffset=25.67 decoffset=-6.41


# science target Mrk 728 with nearby offset stars
SDSS J110101.48+110313.5       11 01 01.48  11 03 13.54  2000.0 raoffset=-4.46 decoffset=24.62
SDSS J110103.27+110250.8       11 01 03.28  11 02 50.89  2000.0 raoffset=22.43 decoffset=01.98


# science target MCG+04-22-042 with nearby offset stars
SDSS J092341.33+225442.3       09 23 41.33  22 54 42.30  2000.0 raoffset=-25.06 decoffset=09.65
SSTSL2 J092342.53+225403.4     09 23 42.54  22 54 03.46  2000.0 raoffset=-7.02 decoffset=-29.20
2MASS J09234298+2254352        09 23 42.99  22 54 35.21  2000.0 raoffset=-0.22 decoffset=02.56
SSTSL2 J092343.01+225501.6     09 23 43.02  22 55 01.70  2000.0 raoffset=00.18 decoffset=29.05
2MASS J09234304+2254294        09 23 43.05  22 54 29.41  2000.0 raoffset=00.68 decoffset=-3.24
2MASS J09234310+2254085        09 23 43.12  22 54 08.46  2000.0 raoffset=01.73 decoffset=-24.19
```

After a small modification manually, this is the starlist

```cs
# science targets
PG1404+226                     14 06 21.91  22 23 46.2   2000.0
SDSS J125603.52+275506.5       12 56 03.52  27 55 06.5   2000.0
2MASX J15335467+2356150        15 33 54.68  23 56 14.7   2000.0
Mrk 877                        16 20 11.28  17 24 27.5   2000.0
RBS 1303                       13 41 12.88 -14 38 40.2   2000.0

# science target RIXOS F236_021 with nearby offset stars
RIXOS F236_021                 17 00 35.80  51 48 30.00  2000.0
2MASS J17003334+5148150        17 00 33.35  51 48 15.05  2000.0 raoffset=-42.34 decoffset=-11.56

# science target 3C 319 with nearby offset stars
3C 319                         15 24 05.60  54 28 18.40  2000.0
SDSS J152402.37+542815.6       15 24 02.37  54 28 15.67  2000.0 raoffset=-49.00 decoffset=-2.74
[VFK2015] J231.01678+54.46757  15 24 04.03  54 28 03.25  2000.0 raoffset=-24.19 decoffset=-15.16
2MASS J15240491+5428057        15 24 04.91  54 28 05.34  2000.0 raoffset=-10.91 decoffset=-13.07
SDSS J152405.15+542829.3       15 24 05.15  54 28 29.39  2000.0 raoffset=-7.34 decoffset=10.98
SDSS J152405.72+542814.3       15 24 05.72  54 28 14.38  2000.0 raoffset=01.26 decoffset=-4.03
3C 319:[KM95] G1               15 24 05.78  54 28 14.52  2000.0 raoffset=02.12 decoffset=-3.89
SDSS J152406.04+542801.4       15 24 06.05  54 28 01.45  2000.0 raoffset=06.08 decoffset=-16.96
SDSS J152406.44+542750.8       15 24 06.45  54 27 50.80  2000.0 raoffset=12.13 decoffset=-27.61
3C 319:[KM95] G2               15 24 06.67  54 28 19.60  2000.0 raoffset=15.52 decoffset=01.19
SDSS J152406.67+542819.1       15 24 06.68  54 28 19.20  2000.0 raoffset=15.59 decoffset=00.79
SDSS J152406.93+542805.7       15 24 06.94  54 28 05.74  2000.0 raoffset=19.48 decoffset=-12.67

# science target Hercules A with nearby offset stars
Hercules A                     16 51 08.02  04 59 34.90  2000.0
SSTSL2 J165106.93+045912.7     16 51 06.93  04 59 12.70  2000.0 raoffset=-18.25 decoffset=-20.63
SSTSL2 J165106.99+045938.2     16 51 06.99  04 59 38.29  2000.0 raoffset=-17.32 decoffset=04.97
GALEXMSC J165107.19+045931.3   16 51 07.20  04 59 31.31  2000.0 raoffset=-14.29 decoffset=-2.02
SSTSL2 J165107.59+045920.3     16 51 07.59  04 59 20.36  2000.0 raoffset=-8.35 decoffset=-12.96
1WGA J1651.1+0459              16 51 07.70  04 59 33.00  2000.0 raoffset=-6.73 decoffset=-0.32
SSTSL2 J165107.86+045913.2     16 51 07.86  04 59 13.27  2000.0 raoffset=-4.32 decoffset=-20.05
HERCULES A Second Nucleus      16 51 07.98  04 59 35.59  2000.0 raoffset=-2.52 decoffset=02.27
SSTSL2 J165107.98+045910.3     16 51 07.99  04 59 10.32  2000.0 raoffset=-2.38 decoffset=-23.00
SSTSL2 J165108.03+045916.6     16 51 08.04  04 59 16.62  2000.0 raoffset=-1.62 decoffset=-16.70
Hercules A Cluster             16 51 08.16  04 59 32.42  2000.0 raoffset=00.18 decoffset=-0.90
SSTSL2 J165108.86+045918.5     16 51 08.87  04 59 18.56  2000.0 raoffset=10.80 decoffset=-14.76
SSTSL2 J165109.08+045938.0     16 51 09.08  04 59 38.08  2000.0 raoffset=14.04 decoffset=04.75
SSTSL2 J165109.09+045908.4     16 51 09.09  04 59 08.41  2000.0 raoffset=14.18 decoffset=-24.91
SSTSL2 J165109.23+045930.6     16 51 09.23  04 59 30.66  2000.0 raoffset=16.27 decoffset=-2.66
SSTSL2 J165109.36+045921.2     16 51 09.37  04 59 21.19  2000.0 raoffset=18.29 decoffset=-12.13
2MASS J16510949+0459536        16 51 09.51  04 59 53.74  2000.0 raoffset=20.41 decoffset=20.41
SSTSL2 J165109.60+045931.1     16 51 09.60  04 59 31.16  2000.0 raoffset=21.85 decoffset=-2.16
SSTSL2 J165109.74+045932.4     16 51 09.74  04 59 32.39  2000.0 raoffset=23.94 decoffset=-0.94
SSTSL2 J165109.86+045926.9     16 51 09.86  04 59 26.92  2000.0 raoffset=25.67 decoffset=-6.41

# science target Mrk 728 with nearby offset stars
Mrk 728                        11 01 01.77  11 02 48.90  2000.0
SDSS J110101.48+110313.5       11 01 01.48  11 03 13.54  2000.0 raoffset=-4.46 decoffset=24.62
SDSS J110103.27+110250.8       11 01 03.28  11 02 50.89  2000.0 raoffset=22.43 decoffset=01.98

# science target MCG+04-22-042 with nearby offset stars
MCG+04-22-042                  09 23 43.00  22 54 32.60  2000.0
SDSS J092341.33+225442.3       09 23 41.33  22 54 42.30  2000.0 raoffset=-25.06 decoffset=09.65
SSTSL2 J092342.53+225403.4     09 23 42.54  22 54 03.46  2000.0 raoffset=-7.02 decoffset=-29.20
2MASS J09234298+2254352        09 23 42.99  22 54 35.21  2000.0 raoffset=-0.22 decoffset=02.56
SSTSL2 J092343.01+225501.6     09 23 43.02  22 55 01.70  2000.0 raoffset=00.18 decoffset=29.05
2MASS J09234304+2254294        09 23 43.05  22 54 29.41  2000.0 raoffset=00.68 decoffset=-3.24
2MASS J09234310+2254085        09 23 43.12  22 54 08.46  2000.0 raoffset=01.73 decoffset=-24.19
```

## (f) Make a detailed plan for the night, indicating when you will be observing each object, like the plan I showed in class. Using the S/N calculator for LRIS (link below), choose your exposure times so that you will get a S/N > 50 for each target in the region around 6000Å. You can find the LRIS Exposure Time Calculator at http://etc.ucolick.org/web_s2n/lris . You can use the default Diachroic, Grism, and Grating (we will cover these in class later). Change the slit width to 1.0 arcsec. You may assume a seeing of 0.7 arcsec, and you should enter the airmass value at which you think you will observe your target. You can figure out the rest of the parameters from the information you gather on NED

To make a plan as the instructor shown in the class,
it seems we have to do the conversion between local time and local mean sidereal time.

I think people probably have a better way to do it,
but I just calculated in this way:

```python
from datetime import date

# from difference bettwen JD and JD2000 to offset of GMST and UT
JD20002GMST = lambda d :  24110.54841 + 8640184.812866 * (d / 36525) \
    + 0.093104 * (d / 36525)**2 - 0.0000062 * (d / 36525)**3

def LT2LMST(year, month, day, hh, mm, ss, offset_mm=-21, offset_ss=-53):
    '''
    convert local time to local mean sidereal time

    Parameters:
    ----
    year  (int)
    month (int)
    day   (int)
    hh    (int)
    mm    (int)
    ss    (int)

    offset_mm (int) : offset mm due to longitude of the observatory, east longitude
    offset_ss (int) : offset ss due to longitude of the observatory, east longitude

    Return:
    ----
    LMST  (tuple) :  (hh, mm, ss)
    '''
    this_date   = date(year, month, day)
    ref_date    = date(2000,     1,   1)

    delta_days  = this_date - ref_date  
    delta_days  = delta_days.days

    delta_frac_day = (hh + mm / 60 + ss / 3600) / 24   - 12 / 24

    # this would be the difference between JD and JD2000
    delta_days  += delta_frac_day

    # calc offset in secs within a day
    delta_secs  = JD20002GMST(delta_days)

    # consider the longitude of the observatory
    delta_secs  += offset_mm * 60 + offset_ss

    delta_hour  =  delta_secs % (60 * 60 * 24) // (60 * 60)
    delta_min   = (delta_secs % (60 * 60 * 24)  % (60 * 60)) // 60
    delta_sec   = (delta_secs % (60 * 60 * 24)  % (60 * 60)) %  60

    # convert to LMST
    new_hh      = hh + delta_hour
    new_mm      = mm + delta_min
    new_ss      = ss + delta_sec

    ss          = (new_ss % 60)
    mm          = (new_mm + (new_ss // 60)) % 60
    hh          = (new_hh + (new_mm + (new_ss // 60)) // 60) % 24

    return hh, mm, ss
```

Probably need to generate a list of observation times from around 1800 (May 22 2020) to 0600 (May 23 2020).
Other people may have a better way,
but I do it in a for loop:

```python
def generate_schedule(local_time_list, local_mean_sidereal_time_list):
    '''
    print the schedule, handle the format
    '''
    column_names = ["LT", "LMST", "Target", "Exposure Time", "Comments"]
    markdown_sep = "---".join( ["|" for i in range(len(column_names) + 1)] )

    schedule_list = [
         "|{}|".format( "|".join( column_names ) ),
         markdown_sep
    ]
    for ls, lmst in zip(local_time_list, local_mean_sidereal_time_list):
        ls_str   = "{:02d}:{:02d}".format( int(ls.hour), int(ls.minute) )
        lmst_str = "{:02d}:{:02d}:{:05.2f}".format( int(lmst[0]), int(lmst[1]), lmst[2] ) 
        row_str = "| {:<10} | {:<10} |    |    |    |".format(ls_str, lmst_str)

        schedule_list.append(row_str)

    schedule_str = "\n".join( schedule_list )

    print(schedule_str)

    return schedule_str
```

| LT                 | LMST        | Target                                 | Exposure Time                    | Comments              |
| ------------------ | ----------- | -------------------------------------- | -------------------------------- | --------------------- |
| 18:00              | 05:40:54.64 |                                        |                                  |                       |
| 18:10              | 05:50:56.28 |                                        |                                  |                       |
| 18:20              | 06:00:57.92 |                                        |                                  |                       |
| 18:30              | 06:10:59.57 |                                        |                                  |                       |
| <mark>18:40</mark> | 06:21:01.21 |                                        |                                  | sunset                |
| 18:50              | 06:31:02.85 |                                        |                                  |                       |
| <mark>19:00</mark> | 06:41:04.49 | standard 1: *BD+08 2015*               | 10 seconds                       | civil twilight        |
| 19:10              | 06:51:06.14 | standard 2: *L745-46A*                 | 10 seconds                       |                       |
| <mark>19:20</mark> | 07:01:07.78 | standard 3: *BD+75 325*                | 10 seconds                       | nautical twilight     |
| 19:30              | 07:11:09.42 |                                        |                                  |                       |
| 19:40              | 07:21:11.07 |                                        |                                  |                       |
| <mark>19:50</mark> | 07:31:12.71 | target 1: **MCG+04-22-042**            | 10 mins setup + 10 mins exposure | astronomical twilight |
| 20:00              | 07:41:14.35 | target 1                               |                                  | to 160 S/N            |
| 20:10              | 07:51:15.99 | target 1                               |                                  |                       |
| 20:20              | 08:01:17.64 | target 2: **Mrk 728**                  | 30 mins exposure                 | to 120 S/N            |
| 20:30              | 08:11:19.28 | target 2                               |                                  |                       |
| 20:40              | 08:21:20.92 | target 2                               |                                  |                       |
| 20:50              | 08:31:22.57 | target 3: **SDSS J125603.52+275506.5** | 35 mins exposure                 | to 120 S/N            |
| 21:00              | 08:41:24.21 | target 3                               |                                  |                       |
| 21:10              | 08:51:25.85 | target 3                               |                                  |                       |
| 21:20              | 09:01:27.49 | target 3                               |                                  |                       |
| 21:30              | 09:11:29.14 | target 4: **PG1404+226**               | 35 mins exposure                 | to 150 S/N            |
| 21:40              | 09:21:30.78 | target 4                               |                                  |                       |
| 21:50              | 09:31:32.42 | target 4                               |                                  |                       |
| 22:00              | 09:41:34.06 | target 4                               |                                  |                       |
| 22:10              | 09:51:35.71 | target 5: **RBS 1303**                 | 20 mins exposure                 | to 250 S/N            |
| 22:20              | 10:01:37.35 | target 5                               |                                  |                       |
| 22:30              | 10:11:38.99 | target 6: **3C 319**                   | 150 mins exposure                | to 120 S/N            |
| 22:40              | 10:21:40.64 | target 6                               |                                  |                       |
| 22:50              | 10:31:42.28 | target 6                               |                                  |                       |
| 23:00              | 10:41:43.92 | target 6                               |                                  |                       |
| 23:10              | 10:51:45.56 | target 6                               |                                  |                       |
| 23:20              | 11:01:47.21 | target 6                               |                                  |                       |
| 23:30              | 11:11:48.85 | target 6                               |                                  |                       |
| 23:40              | 11:21:50.49 | target 6                               |                                  |                       |
| 23:50              | 11:31:52.13 | target 6                               |                                  |                       |
| 00:00              | 11:41:53.78 | target 6                               |                                  |                       |
| 00:10              | 11:51:55.42 | target 6                               |                                  |                       |
| 00:20              | 12:01:57.06 | target 6                               |                                  |                       |
| 00:30              | 12:11:58.71 | target 6                               |                                  |                       |
| 00:40              | 12:22:00.35 | target 6                               |                                  |                       |
| 00:50              | 12:32:01.99 | target 6                               |                                  |                       |
| 01:00              | 12:42:03.63 | target 7: **2MASX J15335467+2356150**  | 90 mins exposure                 | to 120 S/N            |
| 01:10              | 12:52:05.28 | target 7                               |                                  |                       |
| 01:20              | 13:02:06.92 | target 7                               |                                  |                       |
| 01:30              | 13:12:08.56 | target 7                               |                                  |                       |
| 01:40              | 13:22:10.20 | target 7                               |                                  |                       |
| 01:50              | 13:32:11.85 | target 7                               |                                  |                       |
| 02:00              | 13:42:13.49 | target 7                               |                                  |                       |
| 02:10              | 13:52:15.13 | target 7                               |                                  |                       |
| 02:20              | 14:02:16.78 | target 7                               |                                  |                       |
| 02:30              | 14:12:18.42 | target 7                               |                                  |                       |
| 02:40              | 14:22:20.06 | target 7                               |                                  |                       |
| 02:50              | 14:32:21.70 | target 7                               |                                  |                       |
| 03:00              | 14:42:23.35 | target 8: **Mrk 877**                  | 20 mins exposure                 | to 190 S/N            |
| 03:10              | 14:52:24.99 | target 8                               |                                  |                       |
| 03:20              | 15:02:26.63 | target 8                               |                                  |                       |
| 03:30              | 15:12:28.27 | target 9: **Hercules A**               | 30 mins exposure                 | to 70 S/N             |
| 03:40              | 15:22:29.92 | target 9                               |                                  |                       |
| 03:50              | 15:32:31.56 | target 9                               |                                  |                       |
| 04:00              | 15:42:33.20 | target 10: **RIXOS F236_021**          | 50 mins exposure                 | to 70 S/N             |
| 04:10              | 15:52:34.85 | target 10                              |                                  |                       |
| 04:20              | 16:02:36.49 | target 10                              |                                  |                       |
| 04:30              | 16:12:38.13 | target 10                              |                                  |                       |
| 04:40              | 16:22:39.77 | target 10                              |                                  |                       |
| 04:50              | 16:32:41.42 | target 10                              |                                  |                       |
| 05:00              | 16:42:43.06 |                                        |                                  |                       |
| <mark>05:10</mark> | 16:52:44.70 |                                        |                                  | twilight end          |
| 05:20              | 17:02:46.35 |                                        |                                  |                       |
| 05:30              | 17:12:47.99 |                                        |                                  |                       |
| 05:40              | 17:22:49.63 |                                        |                                  |                       |
| 05:50              | 17:32:51.27 |                                        |                                  |                       |
| <mark>06:00</mark> | 17:42:52.92 |                                        |                                  | sunrise               |

## (g) Just like you did in your last homework, play with a few of the parameters of the online calculator to see how they affect the S/N. In particular, describe how binning, seeing, slitwidth, and airmass affect your S/N. Imagine that the seeing is 0.7 arcseconds at the beginning of the night, but at some point it suddenly jumps to 1.5 arcseconds (this does happen!) What would you adjust in your observations to maintain as high a S/N as possible without having to increase the exposure time?

- Seeing ↑ , then S/N ↓
- Binning ↑, then S/N ↑
- Slitwidth ↑, then S/N ↑
- Grism changed, no so much change in S/N, but the shape of spectrum changed
- Grating changed, then S/N ↓

So increase binning pixel would be a way to go.
It makes sense because you adding more photons per pixel.
But I think the trade-off is you lose the resolution in your spectrum.

Increasing the slitwidth would also be a choice to increase S/N.
But increase slitwidth would also lose resolution.
We should be careful about finding an acceptable resolution while changing slitwidth and binning pixel.

## (h) Go back to NED and look up one of the targets. Explore all the information that NED gives you. What was one particular piece of information (other than coordinates, magnitudes, and classification) that you found interesting or helpful?

First object:

```python
from astroquery.ned import Ned

obj = Ned.query_object("RIXOS F236_021")
print(obj)
```

```cs
No.   Object Name        RA        DEC     Type  Velocity   Redshift  Redshift Flag Magnitude and Filter Separation
                      degrees    degrees          km / s                                                   arcmin
--- ---------------- ---------- ---------- ---- ---------- ---------- ------------- -------------------- ----------  
1 LQAC 255+051 002  255.15071   51.80739    G   338166.0      1.128                              18.90         --  

```

I did not particularly found interesting thing in the above query, but this object is the object with the highest redshift in all targets.
One thing I noticed is that the object types are not quite agree with each other in the cross-ids,

```cs
Object Name,                  Object Type
LQAC 255+051 002,             G
RIXOS F236_021,               G
RX J170035.8+514830,          XrayS
1WGA J1700.5+5148,            XrayS
[VCV2001] J170036.2+514826,   QSO
```

I guess they are all correct.
It's just because the way people found it were different.

The SED plot should be useful; However, there're too few data points there, so it's hard to see the overall SED.
