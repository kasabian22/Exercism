from string import ascii_lowercase

def rotate(text, key):
    """A function to implement the rotational cipher, also sometimes called the Caesar cipher."""
    text_list = list(text)
    i = 0
    for character in text_list:
        if character.isalpha():
            num = ascii_lowercase.index(character.lower())
            if character.islower():
                text_list[i] = ascii_lowercase[(num + key) % 26]
            elif character.isupper():
                text_list[i] = ascii_lowercase[(num + key) % 26].upper()
        i += 1
    return "".join(text_list)
