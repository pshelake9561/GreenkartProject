
try:
    x = int(input("Enter a number: "))
    res = 10/x
    print(res)
except ZeroDivisionError:
    print("Devide by zero error")

except ValueError:
    print("Value error")

else:
    print("No exception occured")

finally:
    print("Finally executed")


