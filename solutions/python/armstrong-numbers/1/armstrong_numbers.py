def is_armstrong_number(number):
    power = len(str(number))
    list_num = list(str(number))
    result = [pow(num, power) for num in list(map(int, list_num))]
    return sum(result) == number
