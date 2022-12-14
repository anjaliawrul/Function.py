def dublicates():
    a=[11,23,11,34,7,6,7,9,56,65,56]
    i=0
    b=[]
    f=[]
    c=0
    while i<len(a):
        if a[i] not in b :
            c=c+1
            c=a[i]
            b.append(c)
        else:
            d=a[i]
            f.append(d)
        i=i+1
    print(b)
    print(f)
dublicates()