months = {1: lambda x: 31,
          2: lambda x: 29 if x % 4 == 0 else 28, # x will be passed in as date[2]
          3: lambda x: 31,
          4: lambda x: 30,
          5: lambda x: 31,
          6: lambda x: 30,
          7: lambda x: 31,
          8: lambda x: 31,
          9: lambda x: 30,
          10: lambda x: 31,
          11: lambda x: 30,
          12: lambda x: 31}

def sundayCountNew(start, end):
    date = start
    days = 0
    sundays = 0
    while date != end:
        days += 1
        date[1] += 1
        if date[1] > months[date[0]](date[2]):
            date[1] = 1
            date[0] += 1
        if date[0] > 12:
            date[0] = date[0] % 12
            date[2] += 1
        if date[1] == 1 and days % 7 == 6:
            sundays += 1
    return sundays

def sundayCount(start, end):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    date = start
    days = 0
    sundays = 0
    while date != end:
        days += 1
        date[1] += 1
        if date[2] % 4 == 0 and date[0] == 2:
            if date[1] > 29:
                date[1] = 1
                date[0] += 1
        elif date[1] > months[date[0]]:
            date[1] = 1
            date[0] += 1
        if date[0] > 12:
            date[0] = date[0] % 12
            date[2] += 1
        if date[1] == 1 and days % 7 == 6:
            sundays += 1
    return sundays

print sundayCountNew([12,31,1900],[12,31,2000])
