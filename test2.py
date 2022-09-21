b = [1, 4, 3, 6, 2, 5]
s1 = []
for x in range(3):
    for i in range(len(b)):
        if (i + x) % 3 == 0:
            s1.append(b[i])
            print(i)
