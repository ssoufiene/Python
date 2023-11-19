def add_time(start, duration,day=''):
    c = 0
    n = 0

    if 'PM' in start:
        mode = 'PM'
        start = start.replace('PM', '')
    else:
        mode = 'AM'
        start = start.replace('AM', '')

    start.strip()
    sl = start.split(':')  # list containing start time

    dl = duration.split(':')
    mins = int(sl[1]) + int(dl[1])
    if mins >= 60:
        c = 1
        mins = mins - 60
    hours = int(sl[0]) + int(dl[0]) + c
    if hours > 24:
        n = int(hours / 24)
        hours = hours % 24
    if hours > 12:
        if mode == 'PM':
            hours = hours - 12
            mode1 = 'AM'
        else:
            hours = hours - 12
            mode1 = 'PM'
    elif hours == 12:
        if mode == 'PM':
            mode1 = 'AM'
        else:
            mode1 = 'PM'
    else:
        mode1 = mode
    if mode == 'PM' and mode1 == 'AM':
        n = n + 1
    if day=='':
        if n == 0:
            new_time = f'{hours}:{mins:02d} {mode1}'
        elif n == 1:
            new_time = f'{hours}:{mins:02d} {mode1} (next day)'
        else:
            new_time = f'{hours}:{mins:02d} {mode1} ({n} days later)'
    else :
        day = day.lower()
        listofdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        listofdays2 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        a = listofdays.index(day)
        day=listofdays2[a] 
        if (a + n) > 6:
            ps = ((a + n) % 7) 
        else:
            ps = a + n
        newday = listofdays2[ps]
        if n == 0:
            new_time = f'{hours}:{mins:02d} {mode1}, {day}'
        elif n == 1:
            new_time = f'{hours}:{mins:02d} {mode1}, {newday} (next day)'
        else:
         new_time = f'{hours}:{mins:02d} {mode1}, {newday} ({n} days later)'
    return new_time