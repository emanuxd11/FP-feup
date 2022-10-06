import math

def time_until_lost_connection(direction_A, direction_B):
    direction_A = math.radians(direction_A)
    direction_B = math.radians(direction_B)

    distance_for_each = (35/2) / math.sin(abs(direction_A - direction_B) / 2)

    print(distance_for_each)

    time = distance_for_each / 5 * 60

    return round(time, 3)

print(time_until_lost_connection(int(input()), int(input())))
