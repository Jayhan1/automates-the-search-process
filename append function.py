
"""list = []
n = int(input("Enter number : "))
for i in range(0, n):
    point = int(input())
    list.append(point) 
print(list)"""

"""list = [[i] * 3 for i in range(1, 4)]
output = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(list[i][j])
    output.append(row)

print(output)"""

list = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    i = int(input("Enter i: "))
    j = int(input("Enter j: "))
    point= (i, j)
    list.append(point)

print(list)