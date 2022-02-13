def water_left(astronauts, water_left, days_left):
    for args in [astronauts, water_left, days_left]:
        try:
            #If argument is an int, the following operation works
            args / 10
        except TypeError:
            #Raise only if is not the correct type
            raise TypeError(f"All arguments must be of type int, but received: '{args}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

print(water_left("3","200", None))

