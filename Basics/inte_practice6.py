import copy

ls1 = [[1,2],[33,44]]

ls2 = copy.copy(ls1)
ls2[1][0] = 99
print(ls1)
print(ls2)

ls3 = [[7,8],[10,11]]
ls4 = copy.deepcopy(ls3)
ls4[1][0]=44
print(ls3)
print(ls4)