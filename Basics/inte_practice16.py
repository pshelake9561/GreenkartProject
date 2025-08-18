str = "Ahilyanagarrr"
char_count = {}
for i in str:
    if i in char_count:
        char_count[i] +=1
    else:
        char_count[i] = 1


print(char_count)