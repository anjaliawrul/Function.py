def add():
    a=[3,2,4]
    i=0
    sum=0
    b=[]
    while i<len(a):
        sum+=a[i]
        b.append(i)
        i=i+1
    print(sum)
add()