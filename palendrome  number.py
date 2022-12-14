def palendrome (n):
    rev=0
    a=n
    while (a>0):
        rev=rev*10+a%10
        a=a//10
    if (rev==n):
        print("palendrome number")
    else:
        print("not a palendrome number")
m=int(input("enter the number of reverse"))
palendrome(m)
    