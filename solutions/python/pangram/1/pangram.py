from string import ascii_lowercase, punctuation
def is_pangram(sentence):
    """
    A function to check if a sentence is using every letter at laest once.
    It doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
    """
    all_letters = ascii_lowercase
    for char in sentence.lower().strip(punctuation):
        if char in all_letters:
            all_letters = all_letters.replace(char, "")
    if all_letters == "":
        return True
    return False
