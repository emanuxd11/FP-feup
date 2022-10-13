def convert_12h(hour, minute):
    if hour not in range(0, 24) or minute not in range(0, 60):
        print("INVALID DATE FORMAT")
        return
    
    if hour in range(0, 12):
        half = "am"
        if hour == 0:
            hour = 12
    elif hour in range(12, 24):
        half = "pm"
        if hour != 12:
            hour -= 12

    print(str(hour) + (":%02d" % (minute)) * int(minute != 0), half)

    
convert_12h(int(input()), int(input()))