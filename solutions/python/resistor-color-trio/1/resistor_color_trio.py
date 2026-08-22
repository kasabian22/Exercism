def label(colors):
    resistors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    result = (resistors.index(colors[0]) * 10 + resistors.index(colors[1])) * 10 ** resistors.index(colors[2])
    length = len(str(result))
    if length < 4:
        return str(result) + " ohms"
    elif length < 5:
        return str(result)[:1] + " kiloohms"
    elif length < 6:
        return str(result)[:2] + " kiloohms"
    elif length < 7:
        return str(result)[:3] + " kiloohms"
    elif length < 9:
        return str(result)[:2] + " megaohms"
    else:
        return str(result)[:2] + " gigaohms"