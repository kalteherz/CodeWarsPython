def lose_weight(gender, weight, duration):
    if not (gender == "M" or gender == "F"):
        return 'Invalid genders'
    weight = round(weight, 1)
    if weight <= 0:
        return 'Invalid weight'
    duration = round(duration)
    if duration <= 0:
        return 'Invalid duration'
    if gender == 'M':
        base = 0.985
    else:
        base = 0.988
    weight *= pow(base, duration)
    return round(weight, 1)

print(lose_weight('F', 190, 8))