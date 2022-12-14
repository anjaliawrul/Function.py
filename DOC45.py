def multiply_by():
    a=[23,42,41,1]
    i=0
    while i<len(a):
        if a[i]%2==0:
            print(a[i]*100)
        elif a[i]%2!=0:
            print(a[i]*-1)
        i=i+1
multiply_by()