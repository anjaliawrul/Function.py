def swap_values(arg):
    tem=arg[0]
    arg[0]=arg[1]
    arg[1]=tem
    return arg
x=swap_values([9,8])
print(x)


def swap_values(arg):
    arg[0],arg[1]=arg[1],arg[0]
    return arg 
a=swap_values([3,2])
print(a)