def group_by_first_letter(words):
    dict={}
    
    for word in words:
        letter= word[0].lower()
        if letter not in dict :
            dict[letter] = []
        dict[letter].append(word)
    return dict
     
       
        
        



print(group_by_first_letter(["apple", "avocado", "banana", "blueberry", "cherry"]))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

print(group_by_first_letter(["dog", "cat", "deer", "cow"]))
# {'d': ['dog', 'deer'], 'c': ['cat', 'cow']}

print(group_by_first_letter(["Apple", "ant"]))
# {'a': ['Apple', 'ant']}   (letters are lowercase keys, words keep their original case)

print(group_by_first_letter(["solo"]))
# {'s': ['solo']}

print(group_by_first_letter([]))
# {}