def fact (a):
    if a ==1:
        return a
    else:
        return a* fact(a-1)
n=int(input("enter the number")) 
anju =fact(n)  
print(anju)    

