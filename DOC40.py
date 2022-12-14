def square(a):
    i=0
    while i<len(a):
        b=a[i]
        j=0
        while j<len(b):
            c=int(a[i][j])
            p=c**2
            j=j+1
        i=i+1
        print(p,end="")
square("9119")