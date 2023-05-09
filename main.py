username = ["a","b","c"]
passwords = ("222","333","444")
logind = ["88","99","56"]

users = zip(username, passwords, logind)

print(type(users))

for i in users:
    print(i)