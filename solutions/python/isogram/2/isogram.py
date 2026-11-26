def is_isogram(phrase):
    seen = []
    for char in phrase:
        if char == " " or char == "-":
           continue
        lowercase_character = char.lower()
        if lowercase_character in seen:
           return False    
        seen.append(lowercase_character)
    return True
        