def leap_year(year):
    """Function to check if the year is a leap year or not
    :param (int): year
    return: Bolean Value of wheather the year is lea or not
    """
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False
