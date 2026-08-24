def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if word.casefold() != candidate.casefold() and sorted(word.casefold()) == sorted(candidate.casefold())]
