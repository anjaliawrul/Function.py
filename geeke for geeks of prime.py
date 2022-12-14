def is_prime (a):
    if a in [2,3]:
        return True 
    if (a==1) or (a%2==0):
        return False
    r=3 
    while r*r<=a:
        if a%r==0:
            return False 
        r+=2 
    return True 
print(is_prime (78),is_prime(79))


