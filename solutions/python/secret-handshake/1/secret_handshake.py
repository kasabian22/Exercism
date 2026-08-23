def commands(binary_str):
    handshakes = ["wink", "double blink", "close your eyes", "jump", "Reverse the order"]
    result = []
    for i, number in enumerate(reversed(binary_str)):
        if number == "1" and i != 4: result.append(handshakes[i])
        if number == "1" and i == 4: result.reverse()
    return result
