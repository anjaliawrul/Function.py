# a="The quick Brow Fox"
# upper:3
# lower:12
def chr():
    a="The quick Brow Fox" 
    c=0
    i=0
    while i<len(a):
        if a[i].isupper():
            c+=1
        i=i+1
    print("uppercase chr",c) 
    print("lower chr")
chr()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    


def cases(a):
    upper=0
    lower=0
    for i in a:
        if i.isupper()==True:
            upper=upper+1
        elif i.islower()==True:
            lower=lower+1
    print("upper characters",upper)
    print("lower character",lower)
a=input("enter the string")
cases(a)
