def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    total_squares = 1
    for _ in range(1, number):
        total_squares *= 2
    return total_squares
    # better solution
    # return 1 << (number - 1)
    # return 2 ** (number - 1)


def total():
    total_squares = 1
    for _ in range(1, 65):
        total_squares *= 2
    return total_squares - 1
    # better solutions
    # return (1 << 64) - 1
    # return 2 ** 64 - 1
