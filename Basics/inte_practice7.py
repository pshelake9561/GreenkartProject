
fruits = ["apple", "banana", "cherry"]
#Add to list
fruits.append("mango")
fruits.insert(1,"Orange")
fruits.extend(["Grapes", "kiwi"])

#Update list
fruits[3]="Pramod"
print(fruits)

#Delete
fruits.remove("banana")  #Remove by value
del fruits[3]
popped_item=fruits.pop()

print(fruits)