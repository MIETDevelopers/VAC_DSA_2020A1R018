listt=list(map(int,input().split()))
print(listt)
a,b,c,d,e=listt
print(*listt)
print(a,b,c,d,e,sep='---')
#percentage=sum(listt)/len(listt)
percentage = (a+b+c+d+e)/5
print('percentage is', percentage)
if a>33 and b>33 and c>33 and d>33 and e>33 and percentage>40:
    print("Pass")
    if percentage>=40 and percentage<60:
        print("second division")
    elif percentage>=60 and percentage<80:
        print("first division")
    else:
        print("excellent")
else:
    print("You are fail")