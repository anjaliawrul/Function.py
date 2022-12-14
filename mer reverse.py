def reverse():
    a=["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
    i=0
    while i<len(a):
        if a[i].isalpha()==True:
            b=b+a[i]
        i=i+1
    print(b)
reverse()