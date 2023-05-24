
people = [{'name':'John','age':28},{'name':'Mary','age':23},
          {'name':'Bob','age':35},{'name':'Alice','age':32}]
sorted_list = sorted(people,key=lambda x:x['age'])

print("Sorted:",sorted_list)


