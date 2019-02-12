users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

print(users)
 
key = "+55555555"

if key in users:
    user = users[key]
    del users[key]
    print(user, " deleted")
else:
    print("Unknown user")

print(users)