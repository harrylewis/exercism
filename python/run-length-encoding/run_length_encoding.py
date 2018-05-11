def decode(string):
    decompression = ""
    code = ""
    codes = []

    for char in string:
        if char.isalpha() or char == " ":
            code += char
            codes.append(code)
            code = ""
        else:
            code += char
    print(codes)

    for c in codes:
        if c.isalpha() or c == " ":
            decompression += c
        else:
            for i in range(0, int(c[0:-1])):
                decompression += c[-1]

    return decompression


def encode(string):
    if string is "":
        return string

    compression = ""
    letter = string[0]
    count = 1

    for char in string[1:]:
        if char == letter:
            count += 1
        else:
            compression += (str(count) if count != 1 else "") + letter
            letter = char
            count = 1

    compression += (str(count) if count != 1 else "") + letter

    return compression
