'''
generate_observation_run.py : generate a schedule of observation run
'''
from starlist.calc_time import LT2LMST
from datetime import date, datetime, timedelta

# set parameters
init_year  = 2020
init_month = 3
init_day   = 22
init_hh    = 18
init_mm    = 0
init_ss    = 0

initial_time = datetime(init_year, init_month, init_day, init_hh, init_mm, init_ss)

# increment of time 
delta_mm     = 10   # minutes

# end time
end_year  = 2020
end_month = 3
end_day   = 23
end_hh    = 6
end_mm    = 10
end_ss    = 0

end_time    = datetime(end_year, end_month, end_day, end_hh, end_mm, end_ss)

def generate_time_interval(initial_time, end_time, delta_mm):
    '''
    generate a list of time intervals with delta minutes
    '''
    for i in range( int((end_time - initial_time).seconds // 60 // delta_mm) ):
        yield initial_time + timedelta(minutes=i * delta_mm)

# generate a list for schedule
local_time_list = list(generate_time_interval(initial_time, end_time, delta_mm))
local_mean_sidereal_time_list = [
    LT2LMST(ls.year, ls.month, ls.day, ls.hour, ls.minute, ls.second) for ls in local_time_list 
]

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