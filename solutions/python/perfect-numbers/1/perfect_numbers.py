def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    proper_divisors = []
    for num in range(1, number):
        if number % num == 0:
            proper_divisors.append(num)
    if sum(proper_divisors) == number:
        return "perfect"
    elif sum(proper_divisors) > number:
        return "abundant"
    else:
        return "deficient"
