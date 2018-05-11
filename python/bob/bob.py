def hey(phrase):
    if phrase.strip() is "":
        return "Fine. Be that way!"
    if phrase == phrase.upper() and any(c.isalpha() for c in phrase):
        return "Whoa, chill out!"
    if phrase.strip().endswith("?"):
        return "Sure."
    return "Whatever."
