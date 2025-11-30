import json

FILE = "users.json"

with open(FILE, "r") as f:
    users = json.load(f)

name_to_update = input("name to udpate: ")

for user in users:
    if user["username"] == name_to_update:
        user["score"] = 63

with open(FILE, "w") as f:
    json.dump(users, f, indent=4)