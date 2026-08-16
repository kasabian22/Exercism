def is_valid(isbn):
    """Check if the input is a valid ISBN-10."""
    
    isbn = list(isbn.replace("-", ""))
    if len(isbn) != 10:
        return False
    
    if isbn[-1] == "X":
        isbn[-1] = "10"

    if not all(digit.isdigit() for digit in isbn):
        return False
    
    final = sum(((10 - number) * int(digit) for number, digit in enumerate(isbn)))


    return final % 11 == 0
