from string import ascii_uppercase

def is_valid(isbn):
    digits = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
    isbn = list(isbn.replace("-", ""))

    for letter in ascii_uppercase:
        if letter in isbn and letter != "X" or len(isbn) < 10 or len(isbn) > 10 or ("X" in isbn and isbn[-1] != "X"):
            return False

    if isbn[-1] == "X":
        isbn[-1] = "10"

    print(isbn)
    
    final = [int(number) * int(digit) for number, digit in zip(isbn, digits) if number.isdigit()]


    return sum(final) % 11 == 0 and len(isbn) == 10
