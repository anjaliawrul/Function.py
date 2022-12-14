def avg():
    a=[25,22,10,6,35]
    i=0
    c=0
    b=0
    e=[]
    f=[]
    while i<len(a):
        if a[i]%2==0:
            c+=1
            e.append(a[i])
        elif a[i]%2!=0:
            b+=1
            f.append(a[i])
            i=i+1
            print(e,"even no.",c)
            print(f,"odd no.",b)
avg()


    