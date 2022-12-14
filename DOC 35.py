def age():
    a=int(input("enter the number"))
    if a>0 and a<=14:
        print("drink toddy")
    elif a>14 and a<=18:
        print("drink cake")
    elif a>18 and a<=21:
        print("drink beer")
    else:
        print("drink wisky")
age() 