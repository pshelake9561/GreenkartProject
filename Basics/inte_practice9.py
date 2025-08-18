# Write a python program to create a list using lambda and list comrehension

ls = [(lambda x: x * 2)(x) for x in range(11) if x % 2 == 0]
print(ls)