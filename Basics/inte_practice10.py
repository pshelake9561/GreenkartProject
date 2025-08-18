"""num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10  # 1
    rev = rev * 10 + digit  #
    num = num // 10

print(rev)"""



num2 = 9561
rev = int("".join(reversed(str(num2))))
rev = int(str(num2)[::-1])
print(rev)