from string import ascii_lowercase

def rotate(text, key):
    all_letters = list(enumerate(ascii_lowercase))
    text_list = list(text)
    i = 0
    for character in text_list:
        if character.isalpha():
            for num, char in all_letters:
                if character == char:
                    text_list[i] = all_letters[(num + key) % 26][1]
                elif character == char.upper():
                    text_list[i] = all_letters[(num + key) % 26][1].upper()
        i += 1
    return "".join(text_list)
