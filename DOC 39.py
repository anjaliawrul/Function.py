def max_min():
    a=[4,6,2,1,9,63,-134,566]
    i=0
    max=0
    min=a[i]
    while i<len(a):
        num=a[i]
        if num>max:
            max=num
        elif num<min:
            min=num
        i=i+1
    print(max)
    print(min)
max_min()
            