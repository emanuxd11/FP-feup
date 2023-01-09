def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5

def closest_pair(points):
    points.sort(key = lambda x : x[0])
    
    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]
    
    if len(left) == 2:
        dL = dist(left[0], left[1])
    elif len(left) > 2:
        dL = closest_pair(left)
    else:
        dL = 9999999999
    if len(right) == 2:
        dR = dist(right[0], right[1])
    elif len(right) > 2:
        dR = closest_pair(right)
    else:
        dR = 999999999
    dLR = min(dL, dR)

    dM =  []
    for l_point in left:
        for r_point in right:
            dM.append(dist(l_point, r_point))
    dM = min(dM)
    
    return int(round(min(dLR, dM), 0))

print(closest_pair([(1256, 8483), (61, 2321), (9442, 4823), (1940, 700)]))