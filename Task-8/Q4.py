import pandas as pd
l=input("Enter the string : ")
li=l.split()
ser = pd.Series(li)
x = ser.str.capitalize()
for i in x :
    print(i,end = " ")
print()


