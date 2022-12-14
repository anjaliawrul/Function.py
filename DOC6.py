# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even():
    list=[1,2,3,4,5,6,7,8,9]
    i=0
    b=[]
    even=0
    while i<len(list):
        if list[i]%2==0:
            b.append(list[i])
        i=i+1
    print(b)
even()


def even(a):
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)
    return b
print(even([1,2,3,4,5,6,7,8,9]))
            
