with open("file1.txt") as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())