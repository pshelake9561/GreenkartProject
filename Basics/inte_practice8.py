weights = ["5.5 kg", "900 gm", "10 kg", "1200 gm"]
kg = 0
kg1 = 0
for i in weights:
    ls = i.split()
    if ls[1] == "kg":
        kg = kg + float(ls[0])

    if ls[1] == "gm":
        gm = int(ls[0])
        kg1 = kg1+ gm / 1000

total = kg + kg1
print(total)

