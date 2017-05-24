def make_readable(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    seconds %= 60
    return '{:02}:{:02}:{:02}'.format(h, m, seconds)

print(make_readable(9969))