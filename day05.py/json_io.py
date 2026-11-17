import json

profile = {
    "name": "Sam",
    "age": 26,
    "skills": ["python", "sql"],
    "address": {"city": "Tunis", "zip": 1000},
    "active": True,
    "nickname": None,
}

def save_json(filename, data):
    with open("profile.json", "w") as f:
        json.dump(profile, f, indent=2)

save_json("profile.json", profile)

try:
    def load_json(filename):
        with open("profile.json") as f:
            loaded = json.load(f)
        return loaded

    # print(load_json("profile.json"))
    loaded = load_json("profile.json")

    print(loaded)
    print(loaded == profile)              # True
    print(loaded["skills"][1])            # sql
    print(loaded["address"]["city"])      # Tunis
    print(type(loaded["active"]))  

except FileNotFoundError:
    print({})

