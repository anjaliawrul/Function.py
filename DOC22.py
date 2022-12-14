num=1
def fun():
    global num
    num=num+3
    print(num)
fun()
print(num)