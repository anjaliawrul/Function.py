def count():
    a=[1,9,22,16,54,18,12,32,26]
    i=0
    b=[]
    c=[]
    d=[]
    while i<len(a):
        n=a[i]
        if a[i]<10:
            b.append(n)
        elif a[i]>30:
            c.append(n)
        i=i+1
    print(b)
    print(c)
count()