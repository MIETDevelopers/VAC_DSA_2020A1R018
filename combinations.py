#WAP to print all combinations of the number where addition is 26.
def combination(x):
    for i in range(1,x):
        if i==1:
            print('i '*x)
        for j in range(1,i):
            if i+j==x:
                print(i,j)
            for a in range(x):
                if a+i+j==x:
                    print(a,i,j)
            
num=int(input())
combination(num)