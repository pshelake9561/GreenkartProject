input = "PRI|8046001|Account|2024-07-04T06:50:34.0Z, PRI|8046002|Account|2025-04-17T19:59:11.0Z, UNRS|8046002|Account|2025-04-17T19:59:11.0Z, UNRS|8046001|Account|2024-07-04T06:50:34.0Z,MTN|8046002|Logical|2024-07-04T06:50:34.0Z, WLA|8046002|Physical|2024-07-04T06:50:34.0Z"
input = input.split()
#print(input)
for i in input:
    item_list = i.split("|")
    for j in range(len(item_list)):
        if item_list[j] == "PRI" and item_list[j+1] == "8046002":
            print(item_list[3].replace(",",""))
















