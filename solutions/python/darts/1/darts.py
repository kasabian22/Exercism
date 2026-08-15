import math

radius = [(1, 10), (5, 5) , (10, 1)]
def score(x, y):
    distance = math.sqrt(x**2+ y**2)
    for r, s in radius:
        if distance <= r :
            return s
    return 0
