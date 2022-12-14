def range(start,end,step):
    b=[]
    while start<=end:
        b.append(start)
        start+=step
    print(b)
range(2,10,2)
range(1,10,3)