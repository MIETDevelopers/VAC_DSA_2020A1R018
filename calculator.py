while True:
    x=int(input("Enter 1st number: "))
    y=int(input("Enter 2nd number: "))
    print("choose an option")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulos")
    print("6. Exit")
    o=int(input("Enter an option: "))
    if o==1:
        print(x+y)
    elif o==2:
        print(x-y)
    elif o==3:
        print(x*y)
    elif o==4:
        print(x/y)
    elif o==5:
        print(x%y)
    elif o==6:
        break
    else:
        print("invalid option")
print("thank you for using python")