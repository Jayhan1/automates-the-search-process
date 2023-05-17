l = [2, 2, 2, 2, 8]
l1=l[::-1]
c = 0
for i in range (len(l)):
    if((sum(l[:i]) == sum(l[i:])) or (sum(l1[:i]) == sum(l1[i:]))):
        c=1
    else:
        c=0
if c==1:
    print('True')
else:
    print('False')
    
