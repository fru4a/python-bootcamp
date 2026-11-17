import json

data = {"name": "Sam", "age": 26, "skills": ["python", "sql"]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    loaded = json.load(f)

print(loaded)
print(type(loaded))
print(loaded["skills"][0])
print(loaded == data)
with open("data.json") as f:
    raw = f.read()
print(type(raw))        # <class 'str'>
print(raw)
print(type(json.dumps([1, 2, 3])))
print(type(json.loads("[1, 2, 3]")))
print(json.loads('{"a": 5}')["a"] + 1)
