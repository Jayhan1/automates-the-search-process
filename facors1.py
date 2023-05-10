num = int (input("Enter any number"))
facturs =[]

for i in range(1,num+1):
    if num % i ==0:
        facturs.append(i)

for facturs in facturs:
    print(facturs)