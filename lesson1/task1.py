duration = int(input('How many seconds:'))

if duration < 60:
    print(duration, 'sec')
elif duration >= 60 and duration < 3600:
    min = duration // 60
    sec = duration - min*60
    print(min, 'min, ',sec, 'sec')
elif duration >= 3600 and duration < 86400:
    hours = duration // 3600
    min = (duration - hours*3600) // 60
    sec = duration - hours*3600 - min*60
    print(hours, 'hours, ',min, 'min, ',sec, 'sec')
elif duration >= 86400:
    days = duration // 86400
    hours = (duration - days*86400) // 3600
    min = (duration - days*86400 - hours*3600) // 60
    sec = duration - days*86400 - hours*3600 - min*60
    print(days, 'days, ', hours, 'hours, ',min, 'min, ',sec, 'sec')
