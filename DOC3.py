# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)

# def sum():
#     list =[8, 2, 3, 0, 7]
#     sum=0
#     i=0
#     while i<len(list):
#         n=(list[i])
#         sum+=list[i]
#         i=i+1
#     print(sum)
# sum()

def sum_list(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum
print (sum_list([8,2,3,0,7]))
    

    