
res = [n for n in range(10) if n % 2 == 0]
#print(res)


list = [12,22,33,1,6,5,'7','21',13,43,55,56,32,44]
#odd = [i for i in list if i % 2 != 0]
#print(odd)

Num = [i for i in list if type(i) == int]
print(Num)