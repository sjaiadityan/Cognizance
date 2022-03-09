import numpy as np
o=int(input("the number of elements : "))
li1=[]
li2=[]
for i in range(o):
    b=int(input("enter the elements for list 1 : "))
    li1.append(b)
for i in range(o):
    a=int(input("enter the elements for list 2 : "))
    li2.append(a)

arr1 = np.array(li1)
arr2 = np.array(li2)

print("1st Input array : ", arr1)
print("2nd Input array : ", arr2)
arr = np.add(arr1, arr2)
print("output added array : ", arr)