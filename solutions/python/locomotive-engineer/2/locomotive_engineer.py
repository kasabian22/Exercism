"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return [*wagons]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    # 1- reposition the first two items of the first list to the end
    first, second,  *the_rest = each_wagons_id
    # 2- insert the values from the second list behind (on the right hand side of) the locomotive ID (1).
    the_rest_without_one = [num for num in the_rest if num != 1]
    new_list = [1, *missing_wagons, *the_rest_without_one, first, second]
    
    return new_list


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    return {**route, "stops": [*stops.values()]}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    red, blue, orange = wagons_rows
    ordered_wagons = [
        [red[0], blue[0], orange[0]],
        [red[1], blue[1], orange[1]],
        [red[2], blue[2], orange[2]],
    ]
    # bobahop's solution
    # return list(map(list, zip(*wagons_rows)))
    return ordered_wagons
