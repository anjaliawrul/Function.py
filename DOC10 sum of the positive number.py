a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a<c:
    if b>c:
        print(b,"median")
    else:
        print(c,"median")
if b>c and b>a:
    if c>a:
        print(c,"median")
    else:
        print(a,"median")
if c>a and c>b:
    if a>b:
        print(b,"median")