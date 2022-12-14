def chr_palendrome():
    a=["mom","dad","madam","rotator"]
    i=0
    while i<len(a):
        n=a[i]
        r=n[::-1]
        if r==a[i]:
            print(a[i],"is a palendrome number")
        else:
            print(a[i],"not a palendrome number")
        i=i+1
chr_palendrome()
    