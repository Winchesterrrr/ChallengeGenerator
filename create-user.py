import json

FILE = "users.json"

with open(FILE, "r") as f:
    users = json.load(f)

username = input("Enter username: ")
score = 0

users.append({"username": username, "score": score})

with open(FILE, "w") as f:
    json.dump(users, f, indent = 4)

print("user created successfully")