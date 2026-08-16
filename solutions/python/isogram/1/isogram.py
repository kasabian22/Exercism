def is_isogram(phrase):
    for char in phrase:
        if phrase.casefold().replace(" ", "").replace("-", "").count(char) > 1:
            return False
    return True
