class TestException(Exception):
    def __init__(self):
        self.message = "Age must be 18 or above"
        super().__init__(self.message)

age = int(input("Enter a number: "))
try:
    if age < 18:
        raise TestException
    print("Registration successful")
except TestException as e:
    print("Error", e)
