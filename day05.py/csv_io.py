import csv
people_full = [
    {"name": "Sam", "age": 26, "city": "Tunis"},
    {"name": "Lina", "age": 30, "city": "Sfax"},
    {"name": "Omar", "age": 22, "city": "Sousse"},
    ]
def save_csv(filename, rows) :
   
   

  
   with open("people_full.csv", "w", newline="") as f:

    writer = csv.DictWriter(f, fieldnames=["name", "age","city"])
    writer.writeheader()
    writer.writerows(rows)
   
save_csv("people_full.csv", people_full)

def load_csv(filename) :
  result=[]
  with open("people_full.csv", newline="") as f:

    reader = csv.DictReader(f)
    for row in reader:
      row["age"] = int(row["age"])

      result.append(row)
        
    return result
loaded = load_csv("people_full.csv")
print(loaded)
print(loaded == people_full) 
print(loaded[0]["age"] + 1)   # 27
