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
for i in range(len(li2)):
    comparison = arr1[i] == arr2[i]
    check = str(comparison.all())
    if check == 'True':
        print(arr1[i]," matches in  ",i)