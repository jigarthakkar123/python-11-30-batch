#0 1 1 2 3 5 8 13 21 55 89

n=int(input("Enter N :"))

a,b=0,1
while b<n:
    print(b,end=" ")
    a,b=b,a+b
