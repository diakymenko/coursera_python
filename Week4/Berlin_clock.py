def upper_case(str):
    return str.upper()

def to_berlin_clock_time(str):
    berlin_seconds = to_seconds(slice_sec(str))
    berlin_hours = to_hours(slice_hrs(str))
    berlin_minutes = to_minutes(slice_min(str))
    time = put_time_together(berlin_seconds, berlin_hours, berlin_minutes)
    return time

def slice_hrs(str):
    hours = int(str[0:2])
    return hours

def slice_min(str):
    minutes = int(str[3:5])
    return minutes

def slice_sec(str):
    seconds = int(str[6:8])
    return seconds

def to_seconds(number):
    if number % 2 == 0:
        return "Y"
    else:
        return "O"

def put_time_together(berlin_seconds, berlin_hours, berlin_minutes):
    berlin_time = berlin_seconds + " " + berlin_hours +" "+ berlin_minutes
    return berlin_time

def str_r_hours(number, color):
    str = ""
    for i in range(4):
        if i < number:
            str = str + color
        else:
            str = str + "O"
    return str

def to_hours(number):
    hours_5 = number // 5
    hours_1 = number % 5
    str_5 = str_r_hours(hours_5, "R")
    str_1 = str_r_hours(hours_1, "R")
    berlin_hours = str_5 + " " + str_1
    return berlin_hours

def str_r_minutes_11(number):
    str = ""
    for i in range(number):
        if (i + 1) % 3 == 0:
            str = str + "R"
        else:
            str = str + "Y"
    for i in range(11 - number):
        str = str + "O"
    return str

def to_minutes(number):
    minutes_11 = number // 5
    minutes_1 = number % 5
    str_11 = str_r_minutes_11(minutes_11)
    str_1 = str_r_hours(minutes_1, "Y")
    berlin_minutes = str_11 + " " + str_1
    return berlin_minutes