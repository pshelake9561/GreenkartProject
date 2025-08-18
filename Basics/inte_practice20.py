# lambda function : lambda function in python is a small anonymous function that can have multiple arguments
# but only one expression

add = lambda x, y: x + y
print(add(5, 4))

numbers = [3,6,1,2,8,4,2,7]
square_numbers = map(lambda x: x * 2, numbers)
print(list(square_numbers))

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

print(sorted(numbers))