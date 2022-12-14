def max():
    a=[1, 2, 3, 4, 5, 6, 7, 10, -2]
    i=0
    max=0
    while i<len(a):
        n=a[i]
        if n>max:
            max=n
        i=i+1
    print(max)
max()
