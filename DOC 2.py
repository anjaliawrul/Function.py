# Write a Python function to find the Max of three numbers

def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
n=max(n1,n2,n3)
print(n)
    

    