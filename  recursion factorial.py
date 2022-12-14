# def fact(a):
#     if a==0:
#         return 1
#     else:
#         return a*fact(a-1)
# num=int(input("enter the number"))
# if num<0:
#     print("factorial number")
# else:
#     print("not a factorial number",fact(num))
    



def fact(a):
    if a==1 or a==0:
        return 1
    else:
        return a*fact(a-1)
num=int(input("enter the number"))
print(fact(num))