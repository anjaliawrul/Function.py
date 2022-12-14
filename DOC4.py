# Write a Python program to reverse a string.
# Sample String : "1234abcd

def reverse_str(str1):
    if len(str1)==1:
        return str1
    else:
        return reverse_str(str1[1:])+str1[0]
str1=input("enter the string")
str2=reverse_str(str1)
print(str2)



# def reverse():
#     a="1234abcd"
#     b=a[::-1]
#     print(b)
# reverse()
 