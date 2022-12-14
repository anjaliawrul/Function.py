# def count(a,n):
#     odd=0
#     even=0
#     for i in range (n):
#         if (a[i])%2==0:
#             even=even+1
#         else:
#             odd=odd+1
#     print(even,odd)
# n=int(input("enter the number"))
# a=[]
# for i in range (n):
#     b=int(input("enter the number"))
#     a.append(b)
# count(a,n)

def count(a,n):
    odd=0
    even=0
    for i in range (n):
        if (a[i])%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd
n=int(input("enter the number"))
a=[]
for i in range (n):
    b=int(input("enter the number"))
    a.append(b)
m,n=count(a,n)
print("even",n,"odd",m)

            
            
    