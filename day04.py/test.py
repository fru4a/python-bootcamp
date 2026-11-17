#ages = {"Sam": 25, "Lina": 30}

#print(ages["Sam"])
#ages["Omar"] = 22
#ages["Sam"] = 26
#print(ages)
#print(len(ages))
#print("Lina" in ages)
#print(ages["Nour"])
#print(ages.get("Nour"))
#print(ages.get("Nour", 0))
#for name in ages:
 #   print(name)

#for name, age in ages.items():
 #   print(name, age)
#ages = {"Sam": 26, "Lina": 30, "Omar": 22}
#print(list(ages.keys()))
#print(list(ages.values()))
#print(sum(ages.values()))
#nums = [1, 2, 2, 3, 3, 3]
#s = set(nums)
#print(s)
#print(len(s))
#s.add(4)
#s.add(2)
#print(s)
#print(3 in s)
#point = (3, 5)
#x, y = point
#print(x, y)

#a, b = 1, 2
#a, b = b, a
#print(a, b)
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)
evens = [n for n in range(1, 21) if n % 2 == 0]
print(evens)
short = [w for w in ["sun", "moon", "star", "sky"] if len(w) <= 3]
print(short)
words = ["hello", "big", "world"]
print([w.upper() for w in words])
print([len(w) for w in words])
print([w for w in words if "o" in w])

print({n: n * n for n in range(1, 5)})
print({w: len(w) for w in ["sun", "moon"]})
print([n * 2 for n in [1, 2, 3]])
print([n for n in  [4, 8, 15, 16, 23, 42] if n> 10 ])
print({s: len(s) for s in ["apple", "kiwi", "banana"] })
result = []
for ch in "hello":
    result.append(ch.upper())
print (result)