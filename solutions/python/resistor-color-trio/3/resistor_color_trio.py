def label(colors):
    resistors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    ohms = (resistors.index(colors[0]) * 10 + resistors.index(colors[1])) * 10 ** resistors.index(colors[2])
    if ohms > 1_000_000_000:
        ohms //= 1_000_000_000
        return f"{ohms} gigaohms"
    elif ohms > 1_000_000:
        ohms //= 1_000_000
        return f"{ohms} megaohms"
    elif ohms > 1_000:
        ohms //= 1_000
        return f"{ohms} kiloohms"
    return f"{ohms} ohms"