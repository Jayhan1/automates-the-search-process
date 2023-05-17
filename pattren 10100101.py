a = [[0] * 5 for i in range(5)]
for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            a[i][j] = 1
        print(a[i][j], end=" ")
    print()