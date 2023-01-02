def check_collision(r1, r2):
    print(r1, r2)
    if r1['x2'] < r2['x1'] or r2['x2'] < r1['x1']:
        return False
    if r1['y1'] > r2['y2'] or r2['y1'] > r1['y1']:
        return False
    return True

def number_of_collisions(objects):
    count = 0
    for rectangle in objects:
        for others in objects:
            if rectangle == others:
                continue
            if check_collision(rectangle, others):
                count += 1
    return count

print(number_of_collisions([{'x1': 1, 'y1': 1, 'x2': 3, 'y2': 3}, {'x1': 0, 'y1': 2, 'x2': 4, 'y2': 2}]))
