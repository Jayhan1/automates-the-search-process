lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a=[]

def even(num):
    for n in num:
      if n%2==0:
        a.append(n)
    yield a

print(next(even(lst)))       

    