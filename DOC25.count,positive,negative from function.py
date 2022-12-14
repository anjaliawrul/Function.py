# Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.


def number(list):
    positive=0
    negative =0
    for i in list:
        if i>0:
            positive+=1
        else:
            negative+=1
    print("positive=",positive,",","negative=",negative)
number([2,-7,5,-64,-14])

