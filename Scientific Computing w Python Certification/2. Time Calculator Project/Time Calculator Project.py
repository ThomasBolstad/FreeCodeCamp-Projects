def add_time(start, duration, weekday = 'none'):
    time, timecode = start.split()
    hours, minutes = map(int,(time.split(':')))
    
    if timecode == 'PM' and hours != 12:
        hours += 12
    if timecode == 'AM' and hours == 12:
        hours = 0
    start_minutes = (hours * 60) + minutes

    duration_hours, duration_minutes = map(int, duration.split(':'))
    duration_minutes = (duration_hours * 60) + duration_minutes
    
    new_minutes = start_minutes + duration_minutes

    day_add = new_minutes // 1440
    new_minutes = new_minutes % 1440

    hours = new_minutes // 60
    minutes = new_minutes % 60

    if hours < 12:
        timecode = 'AM'
        if  hours == 0:
            hours = 12
    else:
        timecode = 'PM'
        if hours > 12:
            hours -= 12
    
    if minutes < 10:
       minutes = (f'0{minutes}')
    
    updated_time = f'{hours}:{minutes} {timecode}'
    if day_add == 0:
        days_later = ""
    elif day_add == 1:
        days_later = "(next day)"
    else:
        days_later = f'({day_add} days later)'

    if weekday == 'none':
        new_time = f'{updated_time} {days_later}'.strip()
    
    else:
        day_name = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
        lower_weekday = weekday.lower()
        fixed_weekday = lower_weekday[0].upper() + lower_weekday[1:]
        day_value = day_name[fixed_weekday]
        
        new_day_value = (day_value + day_add) % 7

        # Look up the new day name using the value
        new_day = next(day for day, val in day_name.items() if val == new_day_value)

        new_time = f'{updated_time}, {new_day} {days_later}'.strip()
    
    print(new_time)
    
    return new_time
add_time('8:16 AM', '36:02', 'tuesday')