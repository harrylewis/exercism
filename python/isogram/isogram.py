def is_isogram(string):
    mapping = set()
    for letter in list(string):
      if not letter.isalpha():
        continue
      if letter.lower() not in mapping:
        mapping.add(letter.lower())
      else:
        return False

    return True
