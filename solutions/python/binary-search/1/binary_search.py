def find(search_list, value):
    low = 0
    high = len(search_list) - 1
    while low <= high:
        median = (low + high) // 2
        search_list.sort()
        if search_list[median] == value:
            return median
        if search_list[median] > value:
            high = median - 1
        else:
            low = median + 1
    raise ValueError("value not in array")