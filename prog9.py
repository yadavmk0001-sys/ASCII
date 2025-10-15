rows = 5
ch = 65

for i in range(rows):
    for j in range(i + 1):
        print(chr(ch), end=" ")
    ch +=1
    print()