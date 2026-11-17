import csv

rows = [
   {"name": "Sam", "age": 26},
    {"name": "Lina", "age": 30},
]

with open("people.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(rows)
with open("people.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row["age"], type(row["age"]))
        age = int(row["age"])
        print(age + 1)             # 27