num=int(input("enter the number"))
n=0
for i in range(num,0,-1):
    for j in range(num,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(" ",end=" ")