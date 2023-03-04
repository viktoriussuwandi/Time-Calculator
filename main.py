# This entrypoint file to be used in development. Start by reading README.md

# from time_calculator import add_time
# from unittest import main


# print(add_time("11:06 PM", "2:02"))

# Run unit tests automatically
# main(module='test_module', exit=False)

# -----------------------------------------------------------------------------
# MY TESTER CODE
# -----------------------------------------------------------------------------
def add_time1(start, duration, day_input = None) :
  print(day_input)

  # prepare variable for time calculation
  final_time = { 'hour' : '', 'min' : '', 'timing' : '', 'day' : '' }
  start_t = start.replace(' ',':').split(':')
  dur_t   = duration.split(':')

  # prepare value assignment
  hour_start   = int(start_t[0])
  min_start    = int(start_t[1])
  timing_start = start_t[2]
  
  hour_dur    = int(dur_t[0])
  min_dur     = int(dur_t[1])

  # calculate hour, minute, and timing
  hour_add   = hour_start + hour_dur
  min_add    = min_start  + min_dur

  min        = min_add if min_add < 60   else abs(min_add - 60)
  min_over   = 0 if min_add < 60 else int(min_add/60)  
  hour_add  += min_over
  
  hour       = hour_add if hour_add <= 12 else abs(hour_add - 12)
  
  timing     = timing_start
  if   (timing == 'PM' and hour_add >= 12) : timing = 'AM'
  elif (timing == 'AM' and hour_add >= 12) : timing = 'PM'

  # calculate day
  day_list   = ['Sunday', 'Monday', 'tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturDay']
  day        = 0 if hour_add <=24 else int(hour_add/24)
  day_idx    = (7 - 1 - day_list.index(day_input))  and day > 7 else 0
  
    
  
  final_time['hour']   = f'{hour}'
  final_time['min']    = f'{min}' if min >=10 else f'0{min}'
  final_time['timing'] = timing
  final_time['day']    = day

  format = f"{str(final_time['hour'])}:{str(final_time['min'])} {str(final_time['timing'])}"
  if day_input is not None :
    pass

    
  format += f', {day_list[day_idx]}' if day_input is not None else ''
  format += " (next day)" if day == 1 else f" ({day} days latter" if day > 1 else ''
  
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

  for c in checking:
    print(f'{c}\n')

  # print(add_time1("11:06 PM", "2:02"))
  print( add_time1(start9, duration9, day9) )
  print(a9)
  
test()