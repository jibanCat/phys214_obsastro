'''
calc_time.py : calc astronomical times

Something to remember:
GMST(2000) = UT(2000) + 24110.54841 secs ~ 0 + 6.7 hr

24 Apr 2019:
(365 * 19 + 4 * 30 + 24) days passed

the difference bt sidereal days and solar days is:
1 day / 1 yr
1 / 15 hr / 1 day

the difference between UT and GSMT at 24 Apr 2019 is:
(365 * 19 + 4 * 30 + 24) * 1 / 15 (hrs)

the difference within 24 hrs is:
((365 * 19 + 4 * 30 + 24) * 1 / 15) % 24

Conversion between RA to deg:
24 hr = 360 degrees;
1 hr  = 15 degrees;
1 min = 15 arcmins;
1 sec = 15 seconds;
'''
from astroquery.ned import Ned
import astropy.units as u
from datetime import date

# unit : second
JD20002GMST = lambda d :  24110.54841 + 8640184.812866 * (d / 36525) \
    + 0.093104 * (d / 36525)**2 - 0.0000062 * (d / 36525)**3

# deg to arcsec
deg2arcsec = lambda deg : deg * 60 * 60

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
    new_hh    = hh + delta_hour
    new_mm      = mm + delta_min
    new_ss      = ss + delta_sec

    ss          = (new_ss % 60)
    mm          = (new_mm + (new_ss // 60)) % 60
    hh          = (new_hh + (new_mm + (new_ss // 60)) // 60) % 24
    
    return hh, mm, ss

def deg2RA(deg):
    '''
    convert deg to RA (hh:mm:ss.ss)
    '''
    hh =   deg // 15
    mm = ( deg % 15 ) * 60 // 15
    ss = ((deg % 15 ) * 60  % 15) * 60 / 15
    return int(hh), int(mm), ss

def deg2deg_arcmin_arcsec(deg):
    '''
    convert deg to deg0:arcmin:arcsec
    '''
    deg0   =   deg // 1
    arcmin = ( deg  % 1) * 60 // 1
    arcsec = ((deg  % 1) * 60  % 1) * 60
    return int(deg0), int(arcmin), arcsec

def nearby2starlist(target_list, radius=45, equinox=2000):
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
