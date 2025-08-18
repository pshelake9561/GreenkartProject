#find max number from list

ls = [12,11,2,4,33,45,23,67]
largest = list[0]
smallest = list[0]
for i in ls:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print(largest)
print(smallest)