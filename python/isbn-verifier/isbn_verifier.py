def verify(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    if isbn[-1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]:
        return False
    for num in list(isbn[:-1]):
        if num not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return (int(isbn[0])*10 + int(isbn[1])*9 + int(isbn[2])*8 + int(isbn[3])*7 + int(isbn[4])*6 + int(isbn[5])*5 + int(isbn[6])*4 + int(isbn[7])*3 + int(isbn[8])*2 + (int(isbn[9])*1 if isbn[9] != "X" else 10*1)) % 11 == 0
