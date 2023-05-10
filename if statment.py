fileSize  = (input("enter file size"))
filenumer= int(input("enter number of files"))
memorySize =(input("enter memorySize"))

total= fileSize*filenumer

if memorySize < total:
       print("the file to big to store")  
else :
       print("the file can to store")
    