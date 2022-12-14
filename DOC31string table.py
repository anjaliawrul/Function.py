# Your goal is to return multiplication table for number that is always an integer from 1 to 10.For example, a multiplication table (string) for number == 5 looks like below:- 1 * 5 =5

def string(a):
    i=0
    while i<=10:
        print(i,"x",a,"=",i*a)
        i=i+1
string(int(input("enter the number")))