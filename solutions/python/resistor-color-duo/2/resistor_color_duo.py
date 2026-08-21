def value(colors):
    resistors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    if colors[0] != "black":
        return int(str(resistors.index(colors[0])) + str(resistors.index(colors[1])))
    return resistors.index(colors[1])