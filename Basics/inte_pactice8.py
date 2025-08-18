person = {"Name": "Pramod", "age": 34, "city": "Pune"}

# Add
person["email"] = "pramod@gmail.com"

# update
person["Name"] = "Shivam"
print(person)

# delete
del person["city"]
value = person.pop("email", "No key found")
print(person)
print(value)