# Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']


list=['abc', 'xyz', 'aba', '1221']
i=0
c=0
b=[]
while i<len(list):
    j=list[i][0]
    k=list[i][-1]
    if j==k:
        c+=1
        b.append(list[i])
    i=i+1
print(b)
print("reseult","=",c)
    

