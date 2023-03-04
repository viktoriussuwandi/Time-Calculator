# This entrypoint file to be used in development. Start by reading README.md

from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))

# Run unit tests automatically
main(module='test_module', exit=False)

# -----------------------------------------------------------------------------
# MY TESTER CODE
# -----------------------------------------------------------------------------
# min_added_to_hour = 0
# def calc_minute_left (min) :
#   min_left = min - int(min/60)
#   if (min_left < 60) : return min
#   elif min_left >=60 : 
#     min_added_to_hour += 1
#     calc_minute_left(min_left)
  
def add_time1(start, duration, day_input = None) :
  import math

  # prepare variable for day & time calculation
  timing_list = ['AM', 'PM']
  day_list    = ['Sunday', 'Monday', 'tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturDay']
  final_time  = { 'hour' : '', 'min' : '', 'timing' : '', 'day' : '', 'days_after' : '' }
  start_t     = start.replace(' ',':').split(':')
  dur_t       = duration.split(':')
  min_before = 0; min_after = 0; hour_before = 0; hour_after = 0; day_before = 0; day_after = 0;
  
  # prepare value assignment
  hour_before   = int(start_t[0]); hour_dur = int(dur_t[0]);
  min_before    = int(start_t[1]); min_dur  = int(dur_t[1]) 
  timing_before = start_t[2];      timing_after = ''
  day_before    = day_input if day_input is not None else None
  day_after    = ''
  many_days_after = ''

  # calculate minutes
  min_add              = min_before + min_dur
  min_left             = int(min_add%60)
  min_convert_to_hour  = int(min_add/60)
  # ceil_min_convert     = math.ceil(min_add/60)/
  min_after            = 0 if min_left == 60 else (min_left - 60) if min_left > 60 else min_left
  min_added_to_hour    = min_convert_to_hour if min_add >= 60 else 0
  
  # calculate hours
  hour_add             = hour_before + hour_dur + min_added_to_hour
  hour_left            = int(hour_add%24)
  hour_convert_to_day  = int(hour_add/24)
  # ceil_hour_convert    = math.ceil(hour_add/24)
  hour_after           = (hour_left - 12) if hour_left > 12 else hour_left
  hour_added_to_day    = hour_convert_to_day if hour_add >= 24 else 0

  # calculate timing
  if   hour_left < 12: timing_after = f'{timing_before}'
  elif timing_before == 'AM' and hour_left >= 12 and hour_left < 24 : timing_after = 'PM'
  elif timing_before == 'PM' and hour_left >= 12 and hour_left < 24 : timing_after = 'AM'
  else : timing_after = f"{timing_list[ timing_list.index(timing_before) + hour_added_to_day - len(timing_list) ]}"
  
  # calculate day
  day_index_before    = day_list.index(day_before) if day_before is not None else 0
  if (
      (min_add >= 60 and hour_add >= 24) or 
      (hour_left >= 12 and timing_before == 'PM' and timing_after == 'AM')
    )  : day_add = hour_added_to_day + 1
  else : day_add = hour_added_to_day
  
  day_add_index       = int( (day_index_before + day_add) %7)
  day_index_after     = day_add_index - len(day_list)
  day_after           = day_list[ day_index_after ] if day_before is not None else day_before
  
  # calculate after day
  many_days_after = ' (next day)' if day_add == 1 else f' ({day_add} days later)' if day_add > 1 else ''
  
  # --------------------------------------------------------------------------------
  # format the output
  final_time['min']        = f'{min_after}' if min_after >=10 else f'0{min_after}'
  final_time['hour']       = f'{hour_after}'
  final_time['timing']     = f' {timing_after}'
  final_time['day']        = f' {day_after}'
  final_time['days_after'] = f'{many_days_after}'
  
  format = f"{str(final_time['hour'])}:{str(final_time['min'])}{str(final_time['timing'])}"
  format += f",{final_time['day']}" if day_before is not None else ''
  format += f"{many_days_after}"
  
  return format
  
def test() :
  start1, duration1          = ("3:30 PM", "2:12")
  start2, duration2          = ("11:55 AM", "3:12")
  start3, duration3          = ("9:15 PM", "5:30")
  start4, duration4          = ("11:40 AM", "0:25")
  start5, duration5          = ("2:59 AM", "24:00")
  start6, duration6          = ("11:59 PM", "24:05")
  start7, duration7          = ("8:16 PM", "466:02")
  start8, duration8          = ("5:01 AM", "0:00")
  start9,  duration9,  day9  = ("3:30 PM", "2:12", "Monday")
  start10, duration10, day10 = ("2:59 AM", "24:00", "saturDay")
  start11, duration11, day11 = ("11:59 PM", "24:05", "Wednesday")
  start12, duration12, day12 = ("8:16 PM", "466:02", "tuesday")

  a1  = "5:42 PM" 
  a2  = "3:07 PM"
  a3  = "2:45 AM (next day)"
  a4  = "12:05 PM"
  a5  = "2:59 AM (next day)"
  a6  = "12:04 AM (2 days later)"
  a7  = "6:18 AM (20 days later)"
  a8  = "5:01 AM"
  a9  = "5:42 PM, Monday"
  a10 = "2:59 AM, Sunday (next day)"
  a11 = "12:04 AM, Friday (2 days later)"
  a12 = "6:18 AM, Monday (20 days later)"

  checking = [
    {'checking 1' : add_time1(start1,duration1)  == a1},
    {'checking 2' : add_time1(start2, duration2)  == a2},
    {'checking 3' : add_time1(start3, duration3)  == a3},
    {'checking 4' : add_time1(start4, duration4)  == a4},
    {'checking 5' : add_time1(start5, duration5)  == a5},
    {'checking 6' : add_time1(start6, duration6)  == a6},
    {'checking 7' : add_time1(start7, duration7)  == a7},
    {'checking 8' : add_time1(start8, duration8)  == a8},
    {'checking 9' : add_time1(start9,  duration9, day9)  == a9},
    {'checking 10': add_time1(start10, duration10, day10) == a10},
    {'checking 11': add_time1(start11, duration11, day11) == a11},
    {'checking 12': add_time1(start12, duration12, day12) == a12},
  ]
  
# ----------------------------------------------------------------------------------------
  for c in checking:
    print(f'{c}\n')

  print(add_time1("11:06 PM", "2:02"))
  
# test()