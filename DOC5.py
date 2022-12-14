# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique():
    list =[1,2,3,3,3,3,4,5]
    i=0
    b=[]
    while i<len(list):
        if list[i]not in b:
            b.append(list[i])
        i=i+1
    print(b)
unique()



def unique (a):
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    return c
print(unique([1,2,3,3,3,4,5]))
        




    