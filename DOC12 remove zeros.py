# .Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105




def zeros(a):
    i=0
    b=[]
    while i<len(a):
        k=a[i]
        j=0
        while j<k:
            if k%10==0:
                k=k//10
            j=j+1
        b.append(j)
        i=i+1
    print(b)
zeros([1450,960000,1050])

