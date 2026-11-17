def group_by_first_letter(words):
    groups = {}
    for word in words:
        letter = word[0].lower()
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(word)
    return groups

          
print(group_by_first_letter(["Apple", "aBvocado", "banana", "blueberry", "cherRry"]))

