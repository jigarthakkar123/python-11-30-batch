def maxoftwo(a,b):
    if a>b:
        print(a," Is Greater")
    else:
        print(b," Is Greater")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a," Is Greater")
        else:
            print(c," Is Greater")
    elif b>c:
        print(b," Is Greater")
    else:
        print(c," Is Greater")

def oddeven(a):
    if a%2==0:
        print(a," Is Even")
    else:
        print(a," Is Odd")

def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n," Is Not Prime")
                break
        else:
            print(n," Is Prime")
    else:
        print(n," Is Not Prime")

def fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()
        
