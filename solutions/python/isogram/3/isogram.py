def is_isogram(phrase):
    for char in phrase:
        if char.isalpha():
            if phrase.casefold().count(char) > 1:
                return False
    return True
