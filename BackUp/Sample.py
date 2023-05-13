rno=int(input("Enter Roll No : "))
sname=input("Enter Student Name : ")
s1=int(input("Enter Marks Of Subject 1 : "))
s2=int(input("Enter Marks Of Subject 1 : "))
s3=int(input("Enter Marks Of Subject 1 : "))

total=s1+s2+s3
per=total/3

print("\nStudent Name : ",sname)
print("\nRoll No : ",rno)
print("\nTotal : ",total)
print("\nPercentage : ",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")
