def add():
    a=[12,3,5],[13,4,6],[5,4,3]
    i=0
    sum=0
    b=[]
    while i<len(a):
        j=0
        n=a[i]
        while j<len(a):
            sum=sum+a[i][j]
            j=j+1
        b.append(sum)
        i=i+1
    print(sum,b)
add()
        
    

