def format_duration(seconds):
    _time = [0, 0, 0, 0]
    _time[3] = 60
    _time[2] = 60 * _time[3]
    _time[1] = 24 * _time[2]
    _time[0] = 365 * _time[1]

    name = ['year', 'day', 'hour', 'minute', 'second']

    time = [0, 0, 0, 0, 0]
    for i in range(4):
        time[i] = seconds // _time[i]
        seconds -= time[i] * _time[i]
    time[4] = seconds

    out = ''
    for ind in range(5):
        if time[ind] > 0:
            if not out == "":
                last = True
                if ind < 4:
                    for i in range(4 - ind):
                        if time[ind + i + 1] > 0:
                            last = False
                            break
                if last:
                    out += " and "
                else:
                    out += ", "
            out += str(time[ind]) + ' ' + name[ind]
            if time[ind] > 1:
                out += 's'
    if out == '':
        out = 'now'
    return out

# print(format_duration(1))#, "1 second")
# print(format_duration(62))#, "1 minute and 2 seconds")
# print(format_duration(120))#, "2 minutes")
# print(format_duration(3600))#, "1 hour")
print(format_duration(99000660))#, "1 hour, 1 minute and 2 seconds")