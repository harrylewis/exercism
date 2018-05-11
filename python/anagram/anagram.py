def detect_anagrams(word, candidates):
    valid = []

    for candidate in candidates:
        trial = list(word.lower())
        if len(word) != len(candidate):
            continue
        for letter in candidate:
            if letter.lower() in trial:
                trial.remove(letter.lower())
        if len(trial) == 0:
            valid.append(candidate)

    return valid
