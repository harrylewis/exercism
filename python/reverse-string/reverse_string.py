def reverse(input=''):
    if len(input) == 0:
        return ""
    return input[-1] + reverse(input[:-1])
