Upper_Lower_case= ['Orange','BANANA','apple']
case= list(filter( lambda char:char.isupper(),Upper_Lower_case))
new_case=list(filter(lambda char:char.islower(),Upper_Lower_case))
print(Upper_Lower_case)
print(case)
print(new_case)