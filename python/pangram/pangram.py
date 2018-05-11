def is_pangram(sentence):
  sentence = sentence.lower()
  alphabet = set()
  for letter in list(sentence):
    if letter.isalpha() and letter not in alphabet:
      alphabet.add(letter)
  
  return len(alphabet) == 26
