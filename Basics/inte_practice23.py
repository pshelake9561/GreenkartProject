def CalculateAverage(num1, num2, num3):
    avg = num1 + num2 + num3 / 3
    return avg
    # print("The average of {num1}, {num2} and {num3} is {avg}")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(CalculateAverage(num1, num2, num3))