# Default argument:when we want to provide a default value to the argument in case whose values are passed during the call ,it will be initialized by the default value otherwise with the passed value and this concept is called default argument

# def add (a,b=6):
#     c=a+b
#     print(c)
# add(10) 

def add(a,b,c=10):
    d=a+b+c
    print(d)
add(5,10,15)
     