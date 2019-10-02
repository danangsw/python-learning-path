phonebook = {}
phonebook["John"] = 987656311
phonebook["Jack"] = 987634255
phonebook["Jill"] = 987667453

print(phonebook)

del phonebook["Jack"]

for na, nu in phonebook.items():
    print("Phone number of %s is %d" % (na, nu))
    pass

accounts = {
    "John": 12334547788,
    "Jack": 53534555578,
    "Jill": 90787843435
}

print(accounts)

accounts.pop("Jill")

for na, acc in accounts.items():
    print("Account number of %s is %d" % (na, acc))
    pass