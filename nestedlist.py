"""b=[[i]*3 for i in range(4) if i>0 ]
print(b)

x=[[i]*3 for i in range(1,4) ]
for i in range(3):
    for j in range(3):
        print(x[i][j],end=" ")
    print()"""
list = []
n = int(input("Enter the number of elements: "))

for _ in range(n):
    i = int(input("Enter the value for i: "))
    j = int(input("Enter the value for j: "))
    point = [i, j]
    list.append(point)

print([list])