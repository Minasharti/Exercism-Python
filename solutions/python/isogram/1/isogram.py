def is_isogram(phrase):
  letters = []
  for char in phrase.lower():
    if char.isalpha():
      letters.append(char)
  return len(set(letters)) == len(letters)
