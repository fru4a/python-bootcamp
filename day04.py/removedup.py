def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))        # [1, 2, 3, 4]
print(remove_duplicates(["b", "a", "b", "c", "a"])) # ['b', 'a', 'c']
print(remove_duplicates([5, 5, 5]))                 # [5]
print(remove_duplicates([]))                        # []
print(remove_duplicates([3, 1, 2]))                 # [3, 1, 2]
