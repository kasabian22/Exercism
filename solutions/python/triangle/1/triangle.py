def is_tringle(sides):
    if (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1]):
        return True
    return False
    
# all three sides the same length.
def equilateral(sides):
    if is_tringle(sides):
        if sides[0] > 0 and sides[0] == sides[1] == sides[2]:
            return True
    return False

# at least two sides the same length. 
def isosceles(sides):
    if is_tringle(sides):
        if (sides[0] == sides[1]) or (sides[1] == sides[2]) or (sides[0] == sides[2]):
            return True
    return False

# all sides of different lengths.
def scalene(sides):
    if is_tringle(sides):
        if sides[0] != sides[1] != sides[2] != sides[0]:
            return True
    return False
