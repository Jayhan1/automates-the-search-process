b=[[i]*3 for i in range(4) if i>0 ]
print(b)

x=[[i]*3 for i in range(1,4) ]
for i in range(3):
    for j in range(3):
        print(x[i][j],end=" ")
    print()