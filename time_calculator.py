def add_time(start, duration, day_input = None):

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
  min_after            = 0 if min_left == 60 else (min_left - 60) if min_left > 60 else min_left
  min_added_to_hour    = min_convert_to_hour if min_add >= 60 else 0
  
  # calculate hours
  hour_add             = hour_before + hour_dur + min_added_to_hour
  hour_left            = int(hour_add%24)
  hour_convert_to_day  = int(hour_add/24)
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