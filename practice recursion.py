# def a(n):
#     print("ashwini")
# def b (n2):
#     x=a("hello")
#     print("pizza")
# b('mathpati')
# a('hello')

# n=10
# def a():
#     n=10
#     print(n)
# def b():
#     x=a()
#     print("laddu")
# print(n)
# b()


# num=10
# def a():
#     num=10
#     print(num)
# def v():
#     x=a()
#     print("c")
# print(num)
# v()

# def a(n):
#     print("anjali")
# def b():
#     print("a")
#     a(5)
# b()


def fact(a):
    if a==1 or a==0:
        return 1
    else:
        return a*fact(a-1)
num=int(input("enter the number"))
# if num<0:
#     print("factorial number")
# else:
#     print("not a factorial number",fact(num))
print(fact(num))