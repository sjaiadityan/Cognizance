l=[["Roll No","Name","Marks"]]
def add(l):
    while 1:
        roll=int(input("Enter the roll number :"))
        name=input("Enter the name :")
        marks=float(input("Enter the Marks :"))
        l1=[roll,name,marks]
        l.append(l1)
        c=input("do uh want to continue y/n :").lower()
        if c!='y':
            break
    return l

ch=int(input("1.Subdivision i  2.subdivision ii :"))
if ch==1:
    add(l)
    for j in l:
        print ("{:<8} {:<15} {:<4}".format( j[0], j[1],j[2]))
elif ch==2:
    add(l)
    j=l[1]
    print ("{:<8} {:<15} {:<4}".format( j[0], j[1],j[2]))
else:
    print("Invalid input, enter 1 or 2")