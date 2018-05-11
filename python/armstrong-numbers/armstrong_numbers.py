def is_armstrong(number):
    num_str = str(number)
    pow = len(num_str)
    return number == sum([int(digit)**pow for digit in list(num_str)])
