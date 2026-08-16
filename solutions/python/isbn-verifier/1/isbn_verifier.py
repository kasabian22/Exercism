from string import digits, ascii_uppercase

def is_valid(isbn):
    """Check if the input is a valid ISBN-10."""
    digitsy = list(reversed(digits[1:]))
    digitsy.insert(0, "10")

    for letter in ascii_uppercase:
        if letter in isbn and letter != "X":
            return False

    isbny = [number for number in isbn if number.isdigit()]
    if len(isbny) > 1:
        if isbn[-1] == "X":
            isbny.append("10")

    
    final = [int(number) * int(digit) for number, digit in zip(isbny, digitsy)]


    return sum(final) % 11 == 0 and len (isbny) == 10
