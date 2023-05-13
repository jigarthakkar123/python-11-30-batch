import UDF

while True:

    print("*"*50)
    print("1. Max Of Two")
    print("2. Max Of Three")
    print("3. Odd/Even")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        a=int(input("Enter Number : "))
        b=int(input("Enter Number : "))
        UDF.maxoftwo(a,b)
        print("*"*50)
    elif choice==2:
        a=int(input("Enter Number : "))
        b=int(input("Enter Number : "))
        c=int(input("Enter Number : "))
        UDF.maxofthree(a,b,c)
        print("*"*50)
    elif choice==3:
        a=int(input("Enter Number : "))
        UDF.oddeven(a)
        print("*"*50)
    elif choice==4:
        a=int(input("Enter Number : "))
        UDF.prime(a)
        print("*"*50)
    elif choice==5:
        a=int(input("Enter Number : "))
        UDF.fibonacci(a)
        print("*"*50)
    else:
        break
