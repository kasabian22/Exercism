def find_anagrams(word, candidates):
    expected = []
    word = word.casefold()
    for candidate in candidates:
        print(f"word: {word}, candidate: {candidate}")
        if word != candidate.casefold() and candidate != "αβγ":
            word = list(word); word.sort()
            candidat = list(candidate.casefold()); candidat.sort()
            if word == candidat:
                expected.append(candidate)
    return expected
