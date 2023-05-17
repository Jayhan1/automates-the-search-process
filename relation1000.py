a=[[0]*5 for i in range(5)]
for i in range(4):
    for j in range(4):
        if [i]==[j]: 
         a[i][j] =1
        elif [i]>[j]:
         a[i][j] =2 
          
for i in range(4):
    for j in range(4):
      print(a[i][j],end=" ")
    print()   