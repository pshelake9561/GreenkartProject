#Types of arguments
#postional argument
def add(a,b):
    sum = a+b
    print(sum)

add(10,20)


#Default argument
def greet(name, msg='Hello'):
    print(f"{msg}! {name}")

greet("Pramod")

#Keyword Argument

def welcome(name, role):
    print(f"Hello! {name} welcome as {role}")

welcome(name="Pramod", role="Admin")


#Variable length argument
#*args
def total(*args):
    sum=0
    for n in args:
        sum += n

    print(sum)

total(1,7,5,3,7,)

#**kwargs

def user_info(**userdata):
    for key,value in userdata.items():
        print(key,value)


user_info(name="Pramod", age=34, address='Pune')


#all in one

def all_in_one(a,b,*args,**kwargs):
    print(a,b)  
    print(args)
    print(kwargs)

all_in_one(12,11, 99,88,77,66,55,name="Pramod",age=34)
