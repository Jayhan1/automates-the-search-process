
digits= input("enter number")
def sum_d(digits):
   sum=0
   for digit in str(digits):
     sum = sum +int(digit)
   return sum
print(sum_d(digits))


