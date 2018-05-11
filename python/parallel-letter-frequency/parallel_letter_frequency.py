def calculate(text_input):
    counts = {}

    for group in text_input:
        for char in group.lower():
            if char.isalpha():
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1

    return counts
