def invert(d):
    new_dict = {}

    for key, value in d.items():
        new_dict[value] = key

    return new_dict

    

print(invert({"a": 1, "b": 2, "c": 3}))


print(invert({"Sam": 26, "Lina": 30}))


print(invert({"x": "y"}))
print(invert({"a": 1, "b": 1}))

print(invert({}))
