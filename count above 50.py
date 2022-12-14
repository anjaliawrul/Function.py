def count():
    a=[30,40,60,50,70,77,68,98]
    i=0
    count=0
    while count<len(a):
        if a[count]>50:
            i=i+1
        count=count+1
    print(i)
count()
