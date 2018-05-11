def word_count(phrase):
    word = ""
    words = []
    counts = {}

    for i in range(0, len(phrase)):
        char = phrase[i].lower()
        if char.isalnum():
            word += char
        elif char == "'":
            if i < len(phrase) - 1:
                if phrase[i - 1].lower().isalnum() and phrase[i + 1].lower().isalnum():
                    word += char
        else:
            print(word)
            if word is not "":
                words.append(word)
                word = ""
        if word is not "" and i == len(phrase) - 1:
            words.append(word)
            word = ""

    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    
    return counts
